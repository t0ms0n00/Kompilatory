import AST
import SymbolTable
from Memory import *
from Exceptions import  *
from visit import *
import sys
import numpy as np
import operator

sys.setrecursionlimit(10000)

ops = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv,
    "+=": operator.add,
    "-=": operator.sub,
    "*=": operator.mul,
    "/=": operator.truediv,
    ".+": np.add,
    ".-": np.subtract,
    ".*": np.multiply,
    "./": np.divide,
    "==": operator.eq,
    "!=": operator.ne,
    ">": operator.gt,
    "<": operator.lt,
    ">=": operator.ge,
    "<=": operator.le,

    "unary": np.negative,
    "transpose": np.transpose,
    "eye" : np.eye,
    "ones": np.ones,
    "zeros": np.zeros
}


class Interpreter(object):
    def __init__(self):
        self.memory_stack = MemoryStack()

    @on('node')
    def visit(self, node):
        pass

    @when(AST.Program)
    def visit(self, node):
        try:
            node.instructions.accept(self)
        except ReturnValueException as e:
            print("RETURN ", e.value)

    @when(AST.Instructions)
    def visit(self, node):
        for instruction in node.instructions:
            instruction.accept(self)

    @when(AST.Instruction)
    def visit(self, node):
        node.instruction.accept(self)

    @when(AST.Block)
    def visit(self, node):
        if self.memory_stack.get_last_memory_name() not in ["if", "else", "for", "while"]:
            self.memory_stack.push('block')
            node.instructions.accept(self)
            self.memory_stack.pop()
        else:
            node.instructions.accept(self)

    @when(AST.If)
    def visit(self, node):
        if node.condition.accept(self):
            self.memory_stack.push('if')
            node.then_instr.accept(self)
            self.memory_stack.pop()
        elif node.else_instr is not None:
            self.memory_stack.push('if')
            node.else_instr.accept(self)
            self.memory_stack.pop()

    @when(AST.For)
    def visit(self, node):
        self.memory_stack.push('for')
        from_value, to_value = node.range.accept(self)
        self.memory_stack.insert(node.variable, from_value)
        for value in range(from_value, to_value+1):
            try:
                node.instruction.accept(self)
            except BreakException:
                break
            except ContinueException:
                self.memory_stack.set(node.variable, value + 1)
                continue
            self.memory_stack.set(node.variable, value + 1)
        self.memory_stack.pop()

    @when(AST.Range)
    def visit(self, node):
        return node.from_value.accept(self), node.to_value.accept(self)

    @when(AST.While)
    def visit(self, node):
        self.memory_stack.push('while')
        while node.condition.accept(self):
            try:
                node.instruction.accept(self)
            except BreakException:
                break
            except ContinueException:
                continue
        self.memory_stack.pop()

    @when(AST.Break)
    def visit(self, node):
        raise BreakException()

    @when(AST.Continue)
    def visit(self, node):
        raise ContinueException()

    @when(AST.Return)
    def visit(self, node):
        raise ReturnValueException(node.value.accept(self))

    @when(AST.Print)
    def visit(self, node):
        expressions = node.expressions.accept(self)
        for expr in expressions:
            if type(expr) == str:
                print(expr[1:-1], end=' ')
            else:
                print(expr, end=' ')
        print()

    @when(AST.Expr)
    def visit(self, node):
        return node.expression.accept(self)

    @when(AST.Expressions)
    def visit(self, node):
        expressions = []
        for expr in node.expressions:
            expressions.append(expr.accept(self))
        return expressions

    @when(AST.Singleton)
    def visit(self, node):
        return node.singleton

    @when(AST.Vector)
    def visit(self, node):
        vector = [] if node.expressions is None else node.expressions.accept(self)
        return np.array(vector)

    @when(AST.Assign)
    def visit(self, node):
        variable_name = node.variable.name
        index1 = node.variable.index1 - 1 if node.variable.index1 is not None else None
        index2 = node.variable.index2 - 1 if node.variable.index2 is not None else None
        expr = node.expression.accept(self)
        if index2 is not None:
            if node.operator == "=":
                matrix = self.memory_stack.get(variable_name)
                matrix[index1, index2] = expr
                self.memory_stack.insert(variable_name, matrix)
            else:
                oper = node.operator.accept(self)
                matrix = self.memory_stack.get(variable_name)
                matrix[index1, index2] = ops[oper](matrix[index1, index2], expr)
                self.memory_stack.set(variable_name, matrix)
        elif index1 is not None:
            if node.operator == "=":
                matrix = self.memory_stack.get(variable_name)
                matrix[index1] = expr
                self.memory_stack.insert(variable_name, matrix)
            else:
                oper = node.operator.accept(self)
                matrix = self.memory_stack.get(variable_name)
                matrix[index1] = ops[oper](matrix[index1], expr)
                self.memory_stack.set(variable_name, matrix)
        else:
            if node.operator == "=":
                self.memory_stack.insert(variable_name, expr)
            else:
                oper = node.operator.accept(self)
                value = self.memory_stack.get(variable_name)
                new_value = ops[oper](value, expr)
                self.memory_stack.set(variable_name, new_value)

    @when(AST.CalcAssign)
    def visit(self, node):
        return node.operator

    @when(AST.Variable)
    def visit(self, node):
        index1 = node.index1 - 1 if node.index1 is not None else None
        index2 = node.index2 - 1 if node.index2 is not None else None
        if index2 is not None:
            return self.memory_stack.get(node.name)[index1, index2]
        elif index1 is not None:
            return self.memory_stack.get(node.name)[index1]
        return self.memory_stack.get(node.name)

    @when(AST.Comparator)
    def visit(self, node):
        return node.comparator

    @when(AST.Condition)
    def visit(self, node):
        left = node.left.accept(self)
        right = node.right.accept(self)
        comparator = node.comparator.accept(self)
        return ops[comparator](left, right)

    @when(AST.BinOp)
    def visit(self, node):
        left = node.left.accept(self)
        right = node.right.accept(self)
        oper = node.operator
        if type(ops[oper](left, right)) == str:
            return "\"" + ops[oper](left, right).replace("\"", "") + "\""
        return ops[oper](left, right)

    @when(AST.MatrixOp)
    def visit(self, node):
        left = node.left.accept(self)
        right = node.right.accept(self)
        oper = node.operator
        return ops[oper](left, right)

    @when(AST.UMinus)
    def visit(self, node):
        expr = node.expression.accept(self)
        return ops["unary"](expr)

    @when(AST.Transpose)
    def visit(self, node):
        expr = node.expression.accept(self)
        return ops["transpose"](expr)

    @when(AST.MatrixFunc)
    def visit(self, node):
        func = node.func.accept(self)
        dim1 = node.dim1
        dim2 = node.dim2
        if dim2 is None:
            return ops[func](dim1)
        return ops[func]((dim1, dim2))

    @when(AST.Function)
    def visit(self, node):
        return node.func

    @when(AST.Error)
    def visit(self, node):
        pass
