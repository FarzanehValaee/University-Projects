import ply.lex as lex

# List of token names.   This is always required
reserved = {
    'if': 'IF',
    'while': 'WHILE',
    'for':'FOR',
    'int' : 'INT',
    'float' : 'FLOAT',
}

tokens = ['NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'LPAREN', 'RPAREN', 'IDENTIFIER' , 'ASSIGN2' , 'ASSIGN' , 'PLUSPLUS' , 'LBRACKET' , 'RBRACKET', 'OTHEROP' , 'ILLEGALCHAR'] + list(reserved.values())

# Regular expression rules for simple tokens
t_PLUS = r'\+'
t_PLUSPLUS = r'\+\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_ASSIGN2 = r'=='
t_ASSIGN = r'='
t_LBRACKET = r'{'
t_RBRACKET = r'}'
t_OTHEROP = r'\[|<|!|;|>|\]'
t_ILLEGALCHAR = r'@'



# A regular expression rule with some action code
def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_IDENTIFIER(t):
    r'[a-zA-Z_][0-9a-zA-Z_]*'
    t.type = reserved.get(t.value, 'IDENTIFIER')
    return t


# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# A string containing ignored characters (spaces and tabs)
t_ignore = ' \t'


# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()

data = '''
 while[] if_3 @ j++]
    for4>whilr
 }
'''
# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    print(tok)
