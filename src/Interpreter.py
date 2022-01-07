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
    "transpose": np.transpose
}

# czy returny potrzebne?

class Interpreter(object):
    def __init__(self):
        self.memory_stack = MemoryStack()

    @on('node')
    def visit(self, node):
        pass


    @when(AST.Program)
    def visit(self, node):
        node.instructions.accept(self)


    @when(AST.Instructions)
    def visit(self, node):
        for instruction in node.instructions:
            instruction.accept(self)


    @when(AST.Instruction)
    def visit(self, node):
        node.instruction.accept(self)


    @when(AST.Block)
    def visit(self, node):
        node.instructions.accept(self)


    @when(AST.If)
    def visit(self, node):
        if node.condition.accept(self):
            node.then_instr.accept(self)
        elif node.else_instr is not None:
            node.else_instr.accept(self)


    @when(AST.For) # można uprościć chyba
    def visit(self, node):
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



    @when(AST.Range)
    def visit(self, node):
        return node.from_value.accept(self), node.to_value.accept(self)


    @when(AST.While)
    def visit(self, node):
        while node.condition.accept(self):
            try:
                node.instruction.accept(self)
            except BreakException:
                break
            except ContinueException:
                continue


    @when(AST.Break)
    def visit(self, node):
        raise BreakException()


    @when(AST.Continue)
    def visit(self, node):
        raise ContinueException()


    @when(AST.Return)
    def visit(self, node):
        raise ValueException(node.value.accept(self))


    @when(AST.Print)
    def visit(self, node):
        expressions = node.expressions.accept(self)
        for expr in expressions:
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
        pass


    @when(AST.Assign)
    def visit(self, node):
        pass


    @when(AST.CalcAssign)
    def visit(self, node):
        pass


    @when(AST.Variable)
    def visit(self, node):
        # dodać warunek na referencje (index1 i index2 != None)
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
        r1 = node.left.accept(self)
        r2 = node.right.accept(self)
        # try sth smarter than:
        # if(node.op=='+') return r1+r2
        # elsif(node.op=='-') ...
        # but do not use python eval
        pass


    @when(AST.MatrixOp)
    def visit(self, node):
        pass


    @when(AST.UMinus)
    def visit(self, node):
        pass


    @when(AST.Transpose)
    def visit(self, node):
        pass


    @when(AST.MatrixFunc)
    def visit(self, node):
        pass


    @when(AST.Function)
    def visit(self, node):
        pass


    @when(AST.Error)
    def visit(self, node):
        pass