from __future__ import print_function
import AST


def addToClass(cls):
    def decorator(func):
        setattr(cls, func.__name__, func)
        return func
    return decorator


def printWithIndent(indent, value):
    print(indent*"| " + value)


class TreePrinter:
    @addToClass(AST.Node)
    def printTree(self, indent=0):
        raise Exception("printTree not defined in class " + self.__class__.__name__)

    @addToClass(AST.Program)
    def printTree(self, indent=0):
        if self.instructions is not None:
            self.instructions.printTree(indent)
        else:
            print("Empty file.")

    @addToClass(AST.Instructions)
    def printTree(self, indent=0):
        self.instructions.printTree(indent)
        self.instruction.printTree(indent)

    @addToClass(AST.Instruction)
    def printTree(self, indent=0):
        self.instruction.printTree(indent)

    @addToClass(AST.Block)
    def printTree(self, indent=0):
        self.instructions.printTree(indent)

    @addToClass(AST.If)
    def printTree(self, indent=0):
        printWithIndent(indent, "IF")
        self.condition.printTree(indent+1)
        printWithIndent(indent, "THEN")
        self.then_instr.printTree(indent+1)
        if self.else_instr is not None:
            printWithIndent(indent, "ELSE")
            self.else_instr.printTree(indent+1)

    @addToClass(AST.For)
    def printTree(self, indent=0):
        printWithIndent(indent, "FOR")
        printWithIndent(indent + 1, str(self.variable))
        self.range.printTree(indent + 1)
        self.instruction.printTree(indent + 1)

    @addToClass(AST.Range)
    def printTree(self, indent=0):
        printWithIndent(indent, "RANGE")
        self.from_value.printTree(indent + 1)
        self.to_value.printTree(indent + 1)

    @addToClass(AST.While)
    def printTree(self, indent=0):
        printWithIndent(indent, "WHILE")
        self.condition.printTree(indent + 1)
        self.instruction.printTree(indent + 1)

    @addToClass(AST.Break)
    def printTree(self, indent=0):
        printWithIndent(indent, "BREAK")

    @addToClass(AST.Continue)
    def printTree(self, indent=0):
        printWithIndent(indent, "CONTINUE")

    @addToClass(AST.Return)
    def printTree(self, indent=0):
        printWithIndent(indent, "RETURN")
        if self.value is not None:
            self.value.printTree(indent + 1)

    @addToClass(AST.Print)
    def printTree(self, indent=0):
        printWithIndent(indent, "PRINT")
        self.expressions.printTree(indent + 1)

    @addToClass(AST.Expr)
    def printTree(self, indent=0):
        self.expression.printTree(indent)

    @addToClass(AST.Expressions)
    def printTree(self, indent=0):
        self.expressions.printTree(indent)
        self.expression.printTree(indent)

    @addToClass(AST.Singleton)
    def printTree(self, indent=0):
        if self.singleton.__class__ == str:
            printWithIndent(indent, self.singleton)
        else:
            self.singleton.printTree(indent)

    @addToClass(AST.Number)
    def printTree(self, indent=0):
        printWithIndent(indent, str(self.value))

    @addToClass(AST.Numbers)
    def printTree(self, indent=0):
        if self.numbers is not None:
            self.numbers.printTree(indent)
            self.number.printTree(indent)
        elif self.number is not None:
            self.number.printTree(indent)

    @addToClass(AST.Vector)
    def printTree(self, indent=0):
        printWithIndent(indent, "VECTOR")
        self.numbers.printTree(indent + 1)

    @addToClass(AST.Vectors)
    def printTree(self, indent=0):
        self.vectors.printTree(indent)
        self.vector.printTree(indent+1)

    @addToClass(AST.Matrix)
    def printTree(self, indent=0):
        self.vectors.printTree(indent)

    @addToClass(AST.Assign)
    def printTree(self, indent=0):
        if self.operator == "=":
            printWithIndent(indent, "=")
        else:
            self.operator.printTree(indent)
        self.variable.printTree(indent+1)
        self.expression.printTree(indent+1)

    @addToClass(AST.CalcAssign)
    def printTree(self, indent=0):
        printWithIndent(indent, str(self.operator))

    @addToClass(AST.Variable)
    def printTree(self, indent=0):
        if self.index1 is None and self.index2 is None:
            printWithIndent(indent, self.name)
        else:
            printWithIndent(indent, "REF")
            printWithIndent(indent + 1, self.name)
            printWithIndent(indent + 1, str(self.index1))
            if self.index2 is not None:
                printWithIndent(indent + 1, str(self.index2))

    @addToClass(AST.Comparator)
    def printTree(self, indent=0):
        printWithIndent(indent, str(self.comparator))

    @addToClass(AST.Condition)
    def printTree(self, indent=0):
        self.comparator.printTree(indent)
        self.left.printTree(indent+1)
        self.right.printTree(indent+1)

    @addToClass(AST.BinOp)
    def printTree(self, indent=0):
        printWithIndent(indent, str(self.operator))
        self.left.printTree(indent+1)
        self.right.printTree(indent+1)

    @addToClass(AST.MatrixOp)
    def printTree(self, indent=0):
        printWithIndent(indent, str(self.operator))
        self.left.printTree(indent + 1)
        self.right.printTree(indent + 1)

    @addToClass(AST.UMinus)
    def printTree(self, indent=0):
        printWithIndent(indent, '-')
        self.expression.printTree(indent + 1)

    @addToClass(AST.Parentheses)        # czy wypisywać nawiasy czy samo wyrażenie w nich?
    def printTree(self, indent=0):
        printWithIndent(indent, '(')
        self.expression.printTree(indent + 1)
        printWithIndent(indent, ')')

    @addToClass(AST.Transpose)
    def printTree(self, indent=0):
        printWithIndent(indent, 'TRANSPOSE')
        self.expression.printTree(indent + 1)

    @addToClass(AST.MatrixFunc)
    def printTree(self, indent=0):
        self.func.printTree(indent)
        printWithIndent(indent+1, str(self.dim1))
        if self.dim2 is not None:
            printWithIndent(indent+1, str(self.dim2))

    @addToClass(AST.Function)
    def printTree(self, indent=0):
        printWithIndent(indent, self.func)

    @addToClass(AST.Error)
    def printTree(self, indent=0):
        pass
        # fill in the body
