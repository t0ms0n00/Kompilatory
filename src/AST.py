class Node(object):
    pass


class Program(Node):
    def __init__(self, instructions):
        self.instructions = instructions


class Instructions(Node):
    def __init__(self, instructions, instruction=None):
        self.instructions = instructions
        self.instruction = instruction


class Instruction(Node):
    def __init__(self, instruction):
        self.instruction = instruction


class Block(Node):
    def __init__(self, instructions):
        self.instructions = instructions


class If(Node):
    def __init__(self, condition, then_instr, else_instr=None):
        self.condition = condition
        self.then_instr = then_instr
        self.else_instr = else_instr


class Break(Node):
    def __init__(self):
        pass


class Continue(Node):
    def __init__(self):
        pass


class Type(Node):
    def __init__(self, _type):
        self._type = _type


class Number(Node):
    def __init__(self, value):
        self.value = value


class Expr(Node):
    def __init__(self, expression):
        self.expression = expression


class Assign(Node):
    def __init__(self, assignOp, var, expr):
        self.operator = assignOp
        self.variable = var
        self.expression = expr


class CalcAssign(Node):
    def __init__(self, assignOp):
        self.operator = assignOp


class Variable(Node):
    def __init__(self, name, index1=None, index2=None):
        self.name = name
        self.index1 = index1
        self.index2 = index2


class Comparator(Node):
    def __init__(self, comparator):
        self.comparator = comparator


class Condition(Node):
    def __init__(self, comparator, left, right):
        self.comparator = comparator
        self.left = left
        self.right = right


class Error(Node):
    def __init__(self):
        pass
