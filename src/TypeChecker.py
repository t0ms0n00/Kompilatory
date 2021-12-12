import AST
from SymbolTable import *
from OperationTypes import ttype


class NodeVisitor(object):

    def __init__(self):
        # na true w każdym błędzie przed PRINT
        self.error = False

    def visit(self, node):
        method = 'visit_' + node.__class__.__name__
        visitor = getattr(self, method, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):  # Called if no explicit visitor function exists for a node.
        if isinstance(node, list):
            for elem in node:
                self.visit(elem)
        else:
            for child in node.children:
                if isinstance(child, list):
                    for item in child:
                        if isinstance(item, AST.Node):
                            self.visit(item)
                elif isinstance(child, AST.Node):
                    self.visit(child)


class TypeChecker(NodeVisitor):

    def __init__(self):
        self.symbol_table = SymbolTable(None, 'main')
        self.loop_depth = 0

    def visit_Program(self, node):
        if node.instructions is not None:
            self.visit(node.instructions)

    def visit_Instructions(self, node):
        for instruction in node.instructions:
            self.visit(instruction)

    def visit_Instruction(self, node):
        self.visit(node.instruction)

    def visit_Block(self, node):
        self.symbol_table.pushScope("block")
        self.visit(node.instructions)

    def visit_If(self, node):
        self.symbol_table.pushScope('if')
        self.visit(node.condition)
        self.visit(node.then_instr)
        self.symbol_table.popScope()
        if node.else_instr is not None:
            self.symbol_table.pushScope('else')
            self.visit(node.else_instr)
            self.symbol_table.popScope()

    def visit_For(self, node):
        self.loop_depth += 1
        result_type = self.visit(node.range)
        if result_type != 'unknown':
            symbol = VariableSymbol(node.variable, result_type)
            self.symbol_table.put(node.variable, symbol)
        self.visit(node.instruction)
        self.loop_depth -= 1

    def visit_Range(self, node):
        left = self.visit(node.from_value)
        right = self.visit(node.to_value)
        if left != 'int' or right != 'int':
            print("Line {}: Incompatible range types {} and {} for instruction for".format(node.lineno, left, right))
            return 'unknown'
        return 'int'

    def visit_While(self, node):
        self.loop_depth += 1
        self.visit(node.condition)
        self.visit(node.instruction)
        self.loop_depth -= 1

    def visit_Break(self, node):
        # linia-1 może zmienić
        if self.loop_depth == 0:
            print("Line {}: Break outside the loop".format(node.lineno-1))

    def visit_Continue(self, node):
        if self.loop_depth == 0:
            print("Line {}: Continue outside the loop".format(node.lineno-1))

    def visit_Return(self, node):
        if node.value is not None:
            self.visit(node.value)

    def visit_Print(self, node):
        self.visit(node.expressions)

    def visit_Expr(self, node):
        return self.visit(node.expression)

    def visit_Expressions(self, node):
        for expression in node.expressions:
            self.visit(expression)

    def visit_Singleton(self, node):
        if type(node.singleton) == str:
            return 'str'
        elif type(node.singleton) == int:
            return 'int'
        elif type(node.singleton) == float:
            return 'float'
        return 'unknown'

    def visit_Vector(self, node):
        return 'vector'

    def visit_Vectors(self, node):
        for vector in node.vectors:
            self.visit(vector)

    def visit_Matrix(self, node):
        return 'matrix'

    def visit_Assign(self, node):
        #referencje!!!!
        if node.operator == "=":
            right = self.visit(node.expression)
            if right == 'unknown':
                print("Line {}: Cannot assign unknown type to variable".format(node.lineno))
            elif right == 'vector':
                pass
            elif right == 'matrix':
                pass
            else:
                symbol = VariableSymbol(node.variable.name, right)
                self.symbol_table.put(node.variable.name, symbol)
        else: # calc_assign
            operator = self.visit(node.operator)
            if self.visit(node.variable) is None:
                print("Line {}: Variable {} not defined".format(node.lineno, node.variable.name))
                return 'unknown'
            left = self.visit(node.variable)
            right = self.visit(node.expression)
            if right == 'unknown':
                print("Line {}: Cannot assign unknown type to variable".format(node.lineno))
            elif ttype[operator][left][right] == 'unknown':
                print("Line {}: Incompatible assign operation types {} and {} for operator {}".format(node.lineno, left, right, operator))

    def visit_CalcAssign(self, node):
        return node.operator

    def visit_Variable(self, node):
        return self.symbol_table.symbols[node.name].type

    def visit_Comparator(self, node):
        return node.comparator

    def visit_Condition(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        comparator = self.visit(node.comparator)

        result_type = ttype[comparator][left][right]
        if result_type == 'unknown':
            print('Line {}: Incompatible types {} and {} for operation {}'.format(node.lineno, left, right, comparator))

        # czekamy co zwrócą powyższe

    def visit_BinOp(self, node):
        left = self.visit(node.left)
        right = self.visit(node.right)
        operator = node.operator

        result_type = ttype[operator][left][right]
        if result_type == 'unknown':
            print('Line {}: Incompatible types {} and {} for operation {}'.format(node.lineno, left, right, operator))

        return result_type

    def visit_MatrixOp(self, node):
        pass

    def visit_UMinus(self, node):
        expr_type = self.visit(node.expression)
        if ttype['unary'][expr_type][None] == 'unknown':
            print("Line {}: Unary minus cannot be before type {}".format(node.lineno, expr_type))
            return 'unknown'
        return ttype

    def visit_Transpose(self, node):
        pass

    def visit_MatrixFunc(self, node):
        pass
    # eye 2 wymiary

    def visit_Function(self, node):
        pass