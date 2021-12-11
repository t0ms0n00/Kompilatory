import AST
from SymbolTable import *
from OperationTypes import ttype


class NodeVisitor(object):

    def __init__(self):
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
        pass

    def visit_Range(self, node):
        pass

    def visit_While(self, node):
        pass

    def visit_Break(self, node):
        pass

    def visit_Continue(self, node):
        pass

    def visit_Return(self, node):
        pass

    def visit_Print(self, node):
        pass

    def visit_Expr(self, node):
        return self.visit(node.expression)

    def visit_Expressions(self, node):
        pass

    def visit_Singleton(self, node):
        if type(node.singleton) == str:
            return 'str'
        elif type(node.singleton) == int:
            return 'int'
        elif type(node.singleton) == float:
            return 'float'
        return 'unknown'

    def visit_Vector(self, node):
        pass

    def visit_Vectors(self, node):
        pass

    def visit_Matrix(self, node):
        pass

    def visit_Assign(self, node):
        right = self.visit(node.expression)
        if right == 'unknown':
            print("Line {}: Cannot assign unknown type to variable".format(node.lineno))
        elif right == 'matrix' or right == 'vector':
            pass        # macierze i wektory
        else:           # przemyśleć
            symbol = VariableSymbol(node.variable.name, right)
            name = self.get_variable_name(node.variable)
            print(name)
            self.symbol_table.put(node.variable.name, symbol)
        print(self.symbol_table.symbols.items())


    def visit_CalcAssign(self, node):
        pass

    def visit_Variable(self, node):
        pass

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
        pass

    def visit_MatrixOp(self, node):
        pass

    def visit_UMinus(self, node):
        pass

    def visit_Transpose(self, node):
        pass

    def visit_MatrixFunc(self, node):
        pass

    def visit_Function(self, node):
        pass

    def get_variable_name(self, variable):
        name = variable.name
        if variable.index1 is not None:
            name += str(variable.index1)
            if variable.index2 is not None:
                name += str(variable.index2)
        return name
