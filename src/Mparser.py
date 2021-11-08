import scanner
import ply.yacc as yacc

tokens = scanner.tokens

precedence = (
    ('nonassoc', 'IFX'),
    ('nonassoc', 'ELSE'),
    ('nonassoc', '=', 'ADDASSIGN', 'SUBASSIGN', 'MULASSIGN', 'DIVASSIGN'),
    ('nonassoc', '<', '>', 'LESSEQUAL', 'GREATEREQUAL', 'EQUAL', 'NOTEQUAL'),
    ("left", '+', '-'),
    ("left", "DOTADD", "DOTSUB"),
    ("left", '*', '/'),
    ("left", "DOTMUL", "DOTDIV"),
    ('right', 'UMINUS')
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


# def p_print(p): # pozostawiam zakomentowane ale chyba brakuje stopu dla wywoływania się objects, niżej przerobione, zostawiam jeśli nie złapałem idei
#     """ print : PRINT object ';'
#               | PRINT objects ';' """
#
#
# def p_objects(p):
#     """ objects : object ',' objects ';' """

def p_print(p):
    """ print : PRINT objects ';' """


def p_objects_singular(p):
    """ objects : object ';' """


def p_objects_plural(p):
    """ objects : object ',' objects ';' """


def p_object(p):    # bedzie modyfikowane lub dodane zostana produkcje (matrix itp.)
    """ object : STRING
               | ID
               | INTEGER
               | FLOAT
               | expression"""


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


# do przedyskutowania, ogólnie ma służyć do operacji przypisania do elementu macierzy, ale pewnie wyjdzie lepiej jak się macierz zdefiniuje
def p_matrix_element(p):
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

# WAŻNE: Nie wiem, które rozw. lepsze, bo mamy symbol object, który potrafi wywołać expression, więc można:
# 1. przez object dostawać się do expression ponownie i wtedy object zawiera wszystkie typy (ID, STRING, matrix, etc)
# 2. wszędzie na dole prawe strony object zmienić na expression i dodać p_expression_ID itd. , ale wtedy może być
# redundancja bo mamy to w object
# 3. Jakieś inne rozw.


def p_expression_binop(p):
    """expression  : object '+' object
                | object '-' object
                | object '*' object
                | object '/' object"""


def p_expression_matrixop(p):
    """expression : object DOTADD object
                    | object DOTSUB object
                    | object DOTMUL object
                    | object DOTDIV object"""


def p_expression_uminus(p):
    """expression : '-' object %prec UMINUS"""


def p_expression_parentheses(p):
    """expression : '(' object ')'"""


parser = yacc.yacc()
