import scanner
import ply.yacc as yacc
import AST

tokens = scanner.tokens
lexer = scanner.lexer

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
        p[0] = AST.Program()
    p[0].lineno = lexer.lineno


def p_instructions(p):
    """ instructions : instructions instruction
                     | instruction """
    if len(p) == 3:
        p[0] = AST.Instructions(p[1].instructions + [p[2]])
    else:
        p[0] = AST.Instructions([p[1]])
    p[0].lineno = lexer.lineno


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
    p[0].lineno = lexer.lineno


def p_block(p):
    """ block : '{' instructions '}' """
    p[0] = AST.Block(p[2])
    p[0].lineno = lexer.lineno


def p_if(p):
    """ if : IF '(' condition ')' instruction %prec IFX
           | IF '(' condition ')' instruction ELSE instruction """
    if len(p) == 6:
        p[0] = AST.If(p[3], p[5])
    else:
        p[0] = AST.If(p[3], p[5], p[7])
    p[0].lineno = lexer.lineno


def p_for(p):
    """ for : FOR ID '=' range instruction """
    p[0] = AST.For(p[2], p[4], p[5])
    p[0].lineno = lexer.lineno


def p_range(p):
    """ range : expression ':' expression """
    p[0] = AST.Range(p[1], p[3])
    p[0].lineno = lexer.lineno


def p_while(p):
    """ while : WHILE '(' condition ')' instruction """
    p[0] = AST.While(p[3], p[5])
    p[0].lineno = lexer.lineno


def p_break(p):
    """ break : BREAK ';' """
    p[0] = AST.Break()
    p[0].lineno = lexer.lineno


def p_continue(p):
    """ continue : CONTINUE ';' """
    p[0] = AST.Continue()
    p[0].lineno = lexer.lineno


def p_return(p):
    """ return : RETURN ';'
               | RETURN expression ';' """
    if len(p) == 3:
        p[0] = AST.Return()
    else:
        p[0] = AST.Return(p[2])
    p[0].lineno = lexer.lineno


def p_print(p):
    """ print : PRINT expressions ';' """
    p[0] = AST.Print(p[2])
    p[0].lineno = lexer.lineno


def p_expression(p):
    """ expression : singleton
                   | vector
                   | matrix
                   | variable """
    p[0] = AST.Expr(p[1])
    p[0].lineno = lexer.lineno


def p_expressions(p):
    """ expressions : expressions ',' expression
                    | expression """
    if len(p) == 4:
        p[0] = AST.Expressions(p[1].expressions + [p[3]])
    else:
        p[0] = AST.Expressions([p[1]])
    p[0].lineno = lexer.lineno


def p_singleton(p):
    """ singleton : STRING
                  | INTEGER
                  | FLOAT  """
    p[0] = AST.Singleton(p[1])
    p[0].lineno = lexer.lineno


def p_vector(p):
    """ vector : '[' expressions ']'
               | '[' ']' """
    if len(p) == 4:
        p[0] = AST.Vector(p[2])
    else:
        p[0] = AST.Vector()
    p[0].lineno = lexer.lineno


def p_vectors(p):
    """ vectors : vectors ',' vector
                | vector """
    if len(p) == 4:
        p[0] = AST.Vectors(p[1].vectors + [p[3]])
    else:
        p[0] = AST.Vectors([p[1]])
    p[0].lineno = lexer.lineno


def p_matrix(p):
    """ matrix : '[' vectors ']' """
    p[0] = AST.Matrix(p[2])
    p[0].lineno = lexer.lineno


def p_assign(p):
    """ assign : variable '=' expression ';'
               | variable calculation_assign expression ';' """
    p[0] = AST.Assign(p[2], p[1], p[3])
    p[0].lineno = lexer.lineno


def p_calculation_assign(p):
    """ calculation_assign : ADDASSIGN
                           | SUBASSIGN
                           | MULASSIGN
                           | DIVASSIGN """
    p[0] = AST.CalcAssign(p[1])
    p[0].lineno = lexer.lineno


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
    p[0].lineno = lexer.lineno


def p_comparator(p):
    """ comparator : '<'
                   | '>'
                   | EQUAL
                   | NOTEQUAL
                   | LESSEQUAL
                   | GREATEREQUAL """
    p[0] = AST.Comparator(p[1])
    p[0].lineno = lexer.lineno


def p_condition(p):
    """ condition : expression comparator expression """
    p[0] = AST.Condition(p[2], p[1], p[3])
    p[0].lineno = lexer.lineno


def p_expression_binop(p):
    """ expression : expression '+' expression
                   | expression '-' expression
                   | expression '*' expression
                   | expression '/' expression """
    p[0] = AST.BinOp(p[2], p[1], p[3])
    p[0].lineno = lexer.lineno


def p_expression_matrixop(p):
    """ expression : expression DOTADD expression
                   | expression DOTSUB expression
                   | expression DOTMUL expression
                   | expression DOTDIV expression """
    p[0] = AST.MatrixOp(p[2], p[1], p[3])
    p[0].lineno = lexer.lineno


def p_expression_uminus(p):
    """ expression : '-' expression %prec UMINUS """
    p[0] = AST.UMinus(p[2])
    p[0].lineno = lexer.lineno


def p_expression_parentheses(p):
    """ expression : '(' expression ')' """
    p[0] = p[2]
    # p[0].lineno = lexer.lineno


def p_expression_transpose(p):
    """ expression : expression "'" """
    p[0] = AST.Transpose(p[1])
    p[0].lineno = lexer.lineno


def p_expression_matrix_functions(p):
    """ expression : matrix_func '(' INTEGER ')'
                   | matrix_func '(' INTEGER ',' INTEGER ')' """ # dopuszcza np zeros(4,5) - macierz prostokątna
    if len(p) == 5:
        p[0] = AST.MatrixFunc(p[1], p[3])
    else:
        p[0] = AST.MatrixFunc(p[1], p[3], p[5])
    p[0].lineno = lexer.lineno


def p_matrix_function(p):
    """ matrix_func : EYE
                    | ONES
                    | ZEROS """
    p[0] = AST.Function(p[1])
    p[0].lineno = lexer.lineno


parser = yacc.yacc()