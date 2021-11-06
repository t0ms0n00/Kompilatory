import scanner
import ply.yacc as yacc

tokens = scanner.tokens

precedence = (
    # to fill ...
    ('nonassoc', 'IFX'),
    ('nonassoc', 'ELSE'),
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
    """ program : instructions_opt """


def p_instructions_opt_1(p):
    """ instructions_opt : instructions """


def p_instructions_opt_2(p):
    """ instructions_opt : """


def p_instructions_1(p):
    """ instructions : instructions instruction """


def p_instructions_2(p):
    """ instructions : instruction """

# -----------------------------------------------------
def p_instruction(p):   # wszystkie reserved ze skanera, w assign bedzie eye, zeros, ones
    """ instruction : block
                    | if
                    | else
                    | for
                    | while
                    | break
                    | continue
                    | return
                    | print
                    | assign """

def p_block(p):
    """ block : '{' instructions '}' """


def p_if(p):
    """ if : IF '(' assignment ')' instruction %prec IFX
           | IF '(' assignment ')' instruction ELSE instruction """


def p_for(p):
    """ for : FOR ID '=' range instruction """


def p_range(p):
    """ range : expression ':' expression"""


def p_while(p):
    """ while : '(' assignment ')' instruction """


def p_break(p):
    """ break : BREAK ';'"""


def p_continue(p):
    """ continue : CONTINUE ';'"""


def p_return(p):
    """ return : RETURN ';'
               | RETURN expression ';' """


def p_print(p):
    """ print : PRINT object ';'
              | PRINT objects ';' """


def p_objects(p):
    """ objects : object ',' objects ';' """


def p_object(p):    # bedzie modyfikowane lub dodane zostana produkcje (matrix itp.)
    """ object : STRING
               | ID
               | expression """


def p_assign(p):    # do zrobienia funkcja i cale drzewo
    """ assign : """


# def p_expression_binop(p):
#     """expression  : expression '+' expression
#                 | expression '-' expression
#                 | expression '*' expression
#                 | expression '/' expression
#                 | '(' expression ')'
#                 | INTEGER
#                 | FLOAT
#                 | ID"""
#     if p[2] == '+'   : p[0] = p[1] + p[3] # czy bez spacji pójdzie powyżej
#     elif p[2] == '-' : p[0] = p[1] - p[3]
#     elif p[2] == '*' : p[0] = p[1] * p[3]
#     elif p[2] == '/' : p[0] = p[1] / p[3]


parser = yacc.yacc()
