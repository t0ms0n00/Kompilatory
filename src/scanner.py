import ply.lex as lex

reserved = {
    'if'        : "IF",
    'else'      : "ELSE",
    'for'       : "FOR",
    'break'     : "BREAK",
    'continue'  : "CONTINUE",
    'return'    : "RETURN",
    'eye'       : "EYE",
    'zeros'     : "ZEROS",
    'ones'      : "ONES",
    'print'     : "PRINT"
}

tokens = ['INTEGER', 'FLOAT', 'STRING', 'ID', 'ADDASSIGN', 'MULASSIGN', 'SUBASSIGN', 'DIVASSIGN', 'DOTADD', 'DOTSUB',
          'DOTMUL', 'DOTDIV', 'LESSEQUAL', 'GREATEREQUAL', 'NOTEQUAL', 'EQUAL',
          ] + list(reserved.values())



literals = "+-*/=<>(){}[]:',;"

t_ADDASSIGN = r'\+='
t_MULASSIGN = r'\*='
t_SUBASSIGN = r'-='
t_DIVASSIGN = r'/='

t_DOTADD = r'\.\+'
t_DOTMUL = r'\.\*'
t_DOTSUB = r'\.-'
t_DOTDIV = r'\./'

t_LESSEQUAL = r'<='
t_GREATEREQUAL = r'>='
t_NOTEQUAL = r'!='
t_EQUAL = r'=='

t_ignore = '  \t'


def t_STRING(t):
    r'".*"'
    return t


def t_FLOAT(t):
    r'((\d*\.\d+)|(\d+\.\d*))((E|e)(\+|-)?\d+)?'        # żeby nie łapało samej . i pozwalało na 0. i .0
    t.value = float(t.value)
    return t


def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_COMMENT(t):
    r'\#.*'
    pass


def t_ID(t):
    r'[a-zA-Z_]\w*'
    t.type = reserved.get(t.value, 'ID')
    return t


def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


def t_error(t):
    print("ERROR ({}): Illegal character {}".format(t.lexer.lineno, t.value[0]))
    t.lexer.skip(1)


lexer = lex.lex()