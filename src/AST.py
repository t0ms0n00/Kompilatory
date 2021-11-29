from dataclasses import dataclass
from typing import Any

class Node(object):
    pass

@dataclass
class Program(Node):
    instructions: Any = None

@dataclass
class Instructions(Node):
    instructions: Any
    instruction: Any = None

@dataclass
class Instruction(Node):
    instruction: Any

@dataclass
class Block(Node):
    instructions: Any

@dataclass
class If(Node):
    condition: Any
    then_instr: Any
    else_instr: Any = None


class For(Node):
    def __init__(self, iter_var, in_range, do_instr):
        self.variable = iter_var
        self.range = in_range
        self.instruction = do_instr

@dataclass
class Range(Node):
    from_value: Any
    to_value: Any

@dataclass
class While(Node):
    condition: Any
    instruction: Any

@dataclass
class Break(Node):
    pass

@dataclass
class Continue(Node):
    pass

@dataclass
class Return(Node):
    value: Any = None

@dataclass
class Print(Node):
    expressions: Any

@dataclass
class Expr(Node):
    expression: Any

@dataclass
class Expressions(Node):
    expressions: Any
    expression: Any = None


@dataclass
class Singleton(Node):
    singleton: Any

@dataclass
class Number(Node):
    value: int or float
    def __str__(self): return str(self.value)


@dataclass
class Numbers(Node):
    numbers: Any = None
    number: Any = None

@dataclass
class Vector(Node):
    numbers: Any

@dataclass
class Vectors(Node):
    vectors: Any
    vector: Any = None

@dataclass
class Matrix(Node):
    vectors: Any

class Assign(Node):
    def __init__(self, assignOp, var, expr):
        self.operator = assignOp
        self.variable = var
        self.expression = expr


class CalcAssign(Node):
    def __init__(self, assignOp):
        self.operator = assignOp

@dataclass
class Variable(Node):
    name: Any
    index1: Any = None
    index2: Any = None

@dataclass
class Comparator(Node):
    comparator: Any

@dataclass
class Condition(Node):
    comparator: Any
    left: Any
    right: Any

@dataclass
class Error(Node):
    pass
