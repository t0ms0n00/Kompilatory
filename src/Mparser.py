import scanner
import ply.yacc as yacc

tokens = scanner.tokens

precedence = (
    # to fill ...
    ("left", '+', '-'),
    ("left", '*', '/')

    # to fill ...
)


def p_error(p):
    if p:
        print("Syntax error at line {0}: LexToken({1}, '{2}')".format(p.lineno, p.type, p.value))
    else:
        print("Unexpected end of input")


def p_program(p):
    """program : instructions_opt"""


def p_instructions_opt_1(p):
    """instructions_opt : instructions """


def p_instructions_opt_2(p):
    """instructions_opt : """


def p_instructions_1(p):
    """instructions : instructions instruction """


def p_instructions_2(p):
    """instructions : instruction """

# -----------------------------------------------------
def p_instruction(p):
    """instruction : ID '=' expression ';'
                    | """


def p_assign(p):
    """assign : """


def p_expression_binop(p):
    """expression  : expression '+' expression
                | expression '-' expression
                | expression '*' expression
                | expression '/' expression
                | '(' expression ')'
                | INTEGER
                | FLOAT
                | ID"""
    if p[2] == '+'   : p[0] = p[1] + p[3] # czy bez spacji pójdzie powyżej
    elif p[2] == '-' : p[0] = p[1] - p[3]
    elif p[2] == '*' : p[0] = p[1] * p[3]
    elif p[2] == '/' : p[0] = p[1] / p[3]


parser = yacc.yacc()
