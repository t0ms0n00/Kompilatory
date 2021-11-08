import scanner
import ply.yacc as yacc

tokens = scanner.tokens

precedence = (
    # to fill ...
    ('nonassoc', 'IFX'),
    ('nonassoc', 'ELSE'),
    ('nonassoc', '=', 'ADDASSIGN', 'SUBASSIGN', 'MULASSIGN', 'DIVASSIGN'),
    ('nonassoc', '<', '>', 'LESSEQUAL', 'GREATEREQUAL', 'EQUAL', 'NOTEQUAL'),
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
    """ if : IF '(' condition ')' instruction %prec IFX
           | IF '(' condition ')' instruction ELSE instruction """


def p_for(p):
    """ for : FOR ID '=' range instruction """


def p_range(p):
    """ range : expression ':' expression"""


def p_while(p):
    """ while : WHILE '(' condition ')' instruction """


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


def p_assign(p):    # do zrobienia funkcja i cale drzewo - chyba jest OK
    """ assign : lvalue '=' object ';'
                | lvalue calculation_assign object ';' """


def p_calculation_assign(p):
    """ calculation_assign : ADDASSIGN
                            | SUBASSIGN
                            | MULASSIGN
                            | DIVASSIGN """


def p_lvalue(p):
    """ lvalue : ID
                | matrix_element """        # tu brak pewności


def p_matrix_element(p):    # do przedyskutowania, ogólnie ma służyć do operacji przypisania do elementu macierzy
    """ matrix_element : ID '[' INTEGER ',' INTEGER ']'"""


def p_condition(p):
    """ condition : object comparator object """


def p_comparator(p):
    """ comparator : '<'
                  | '>'
                  | EQUAL
                  | NOTEQUAL
                  | LESSEQUAL
                  | GREATEREQUAL """


def p_expression_binop(p):  # wszelkiego rodzaju wyrażenia, podzieliłbym na grupy i do różnych funkcji
    """expression  : expression '+' expression
                | expression '-' expression
                | expression '*' expression
                | expression '/' expression"""


parser = yacc.yacc()
