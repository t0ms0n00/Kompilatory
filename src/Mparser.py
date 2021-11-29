import scanner
import ply.yacc as yacc
import AST

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
    """ program : instructions
                | """
    if len(p) == 2:
        p[0] = AST.Program(p[1])
    else:
        p[0] = AST.Program([])


def p_instructions(p):
    """ instructions : instructions instruction
                    | instruction """
    if len(p) == 3:
        p[0] = AST.Instructions(p[1], p[2])
    else:
        p[0] = AST.Instruction(p[1])


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
    p[0] = AST.Instruction(p[1])


def p_block(p):
    """ block : '{' instructions '}' """
    p[0] = AST.Block(p[2])


def p_if(p):
    """ if : IF '(' condition ')' instruction %prec IFX
           | IF '(' condition ')' instruction ELSE instruction """
    if len(p) == 6:
        p[0] = AST.If(p[3], p[5])
    else:
        p[0] = AST.If(p[3], p[5], p[7])


def p_for(p):
    """ for : FOR ID '=' range instruction """
    p[0] = AST.For(p[2], p[4], p[5])


def p_range(p):
    """ range : expression ':' expression """
    p[0] = AST.Range(p[1], p[3])


def p_while(p):
    """ while : WHILE '(' condition ')' instruction """
    p[0] = AST.While(p[3], p[5])

def p_break(p):
    """ break : BREAK ';' """
    p[0] = AST.Break()


def p_continue(p):
    """ continue : CONTINUE ';' """
    p[0] = AST.Continue()


def p_return(p):
    """ return : RETURN ';'
               | RETURN expression ';' """
    if len(p) == 3:
        p[0] = AST.Return()
    else:
        p[0] = AST.Return(p[2])

def p_print(p):
    """ print : PRINT expressions ';' """
    p[0] = AST.Print(p[2])

def p_expressions(p):
    """ expressions : expressions ',' expression
                    | expression """
    if len(p) == 4:
        p[0] = AST.Expressions(p[1], p[3])
    else:
        p[0] = AST.Expr(p[1])

def p_type(p):
    """ type : STRING
             | number """
    p[0] = AST.Type(p[1])


def p_number(p):
    """ number : INTEGER
               | FLOAT """
    p[0] = AST.Number(p[1])


def p_expression(p):
    """ expression : type
               | vector
               | matrix
               | variable """
    p[0] = AST.Expr(p[1])


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


def p_assign(p):
    """ assign : variable '=' expression ';'
               | variable calculation_assign expression ';' """
    p[0] = AST.Assign(p[2], p[1], p[3])


def p_calculation_assign(p):
    """ calculation_assign : ADDASSIGN
                           | SUBASSIGN
                           | MULASSIGN
                           | DIVASSIGN """
    p[0] = AST.CalcAssign(p[1])


def p_variable(p):
    """ variable : ID
               | ID '[' INTEGER ']'
               | ID '[' INTEGER ',' INTEGER ']' """
    if len(p) == 2:
        p[0] = AST.Variable(p[1])
    elif len(p) == 5:
        p[0] = AST.Variable(p[1], p[3])
    else:
        p[0] = AST.Variable(p[1], p[3], p[5])


def p_comparator(p):
    """ comparator : '<'
                   | '>'
                   | EQUAL
                   | NOTEQUAL
                   | LESSEQUAL
                   | GREATEREQUAL """
    p[0] = AST.Comparator(p[1])


def p_condition(p):
    """ condition : expression comparator expression """
    p[0] = AST.Condition(p[2], p[1], p[3])


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
