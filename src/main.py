import ply.lex as lex

tokens = ('PLUS',  'MINUS',  'TIMES',  'DIVIDE', 'LPAREN','RPAREN',  'LSQPAREN', 'RSQPAREN', 'LCPAREN', 'RCPAREN',
          'NUMBER', 'ID', 'ASSIGN', 'ADDASSIGN', 'MULASSIGN', 'SUBASSIGN', 'DIVASSIGN', 'DOTADD', 'DOTSUB',
          'DOTMUL', 'DOTDIV', 'LESS', 'GREATER', 'LESSEQUAL', 'GREATEREQUAL', 'NOTEQUAL', 'EQUAL')

t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'

t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LSQPAREN = r'\['
t_RSQPAREN = r'\]'
t_LCPAREN = r'\{'
t_RCPAREN = r'\}'

t_ASSIGN = r'='
t_ADDASSIGN = r'\+='
t_MULASSIGN = r'\*='
t_SUBASSIGN = r'-='
t_DIVASSIGN = r'/='

t_DOTADD = r'\.\+'
t_DOTMUL = r'\.\*'
t_DOTSUB = r'\.-'
t_DOTDIV = r'\./'

t_LESS = r'\<'
t_GREATER = r'\>'
t_LESSEQUAL = r'\<='
t_GREATEREQUAL = r'\>='
t_NOTEQUAL = r'\!='
t_EQUAL = r'\=='


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_ID(t):
    r'[a-zA-Z_]\w*'
    return t


t_ignore = '  \t'


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t) :
    print("Illegal character '%s'" %t.value[0])
    t.lexer.skip(1)


lexer = lex.lex()
fh = open("./utils/test1.txt", "r")
lexer.input(fh.read())
for token in lexer:
    print("(%d): %s(%s)" %(token.lineno, token.type, token.value))