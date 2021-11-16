import scanner
import ply.yacc as yacc

tokens = scanner.tokens

precedence = (
    ('nonassoc', 'IFX'),
    ('nonassoc', 'ELSE'),
    ('right', '='),
    ('nonassoc', 'ADDASSIGN', 'SUBASSIGN', 'MULASSIGN', 'DIVASSIGN'),
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
    """ program : instructions
                | """


def p_instructions(p):
    """ instructions : instructions instruction
                    | instruction """


def p_instruction(p):
    """ instruction : block
                    | if
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
    """ range : expression ':' expression """


def p_while(p):
    """ while : WHILE '(' condition ')' instruction """


def p_break(p):
    """ break : BREAK ';' """


def p_continue(p):
    """ continue : CONTINUE ';' """


def p_return(p):
    """ return : RETURN ';'
               | RETURN expression ';' """


def p_print(p):
    """ print : PRINT expressions ';' """


def p_expressions(p):
    """ expressions : expressions ',' expression
                    | expression """


def p_type(p):
    """ type : STRING
             | number """


def p_number(p):
    """ number : INTEGER
               | FLOAT """


def p_expression(p):
    """ expression : type
               | vector
               | matrix
               | variable """


def p_numbers(p):
    """ numbers : numbers ',' number
                | number """


def p_vector(p):
    """ vector : '[' numbers ']' """


def p_vectors(p):
    """ vectors : vectors ',' vector
                    | vector """


def p_matrix(p):
    """ matrix : '[' vectors ']' """


def p_assign(p):    # do zrobienia funkcja i cale drzewo - chyba jest OK
    """ assign : variable '=' expression ';'
               | variable calculation_assign expression ';' """


def p_calculation_assign(p):
    """ calculation_assign : ADDASSIGN
                           | SUBASSIGN
                           | MULASSIGN
                           | DIVASSIGN """


def p_variable(p):
    """ variable : ID
               | ID '[' INTEGER ']'
               | ID '[' INTEGER ',' INTEGER ']' """


def p_comparator(p):
    """ comparator : '<'
                   | '>'
                   | EQUAL
                   | NOTEQUAL
                   | LESSEQUAL
                   | GREATEREQUAL """


def p_condition(p):
    """ condition : expression comparator expression """


def p_expression_binop(p):
    """ expression : expression '+' expression
                   | expression '-' expression
                   | expression '*' expression
                   | expression '/' expression """


def p_expression_matrixop(p):
    """ expression : expression DOTADD expression
                    | expression DOTSUB expression
                    | expression DOTMUL expression
                    | expression DOTDIV expression """


def p_expression_uminus(p):
    """ expression : '-' expression %prec UMINUS """


def p_expression_parentheses(p):
    """ expression : '(' expression ')' """


def p_expression_transpose(p):
    """ expression : expression "'" """


def p_expression_matrix_functions(p):
    """ expression : matrix_func '(' INTEGER ')' 
                   | matrix_func '(' INTEGER ',' INTEGER ')' """ # dopuszcza np zeros(4,5) - macierz prostokątna


def p_matrix_function(p):
    """ matrix_func : EYE
                    | ONES
                    | ZEROS """


parser = yacc.yacc()
