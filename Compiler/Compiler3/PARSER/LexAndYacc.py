import ply.lex as lex


# List of token names.   This is always required
tokens = [ 'ID', 'LESSEQUAL','GREATEREQUAL', 'ASSIGN','EQUALS','NOTEQUAL',
        'GREATERTHAN','LESSTHAN','ADD','MINUS','MULT','DIVIDE','OPENPAR','CLOSEPAR','OPENBRACKET'
        ,'CLOSEBRACKET','SEMI','PEQUAL','MEQUAL','FLOAT','WHILE','IF','ELSE','CHARACTER','VOID','COMMA','TRUE','FALSE','NULL' , 'NEW' ,'STRING' ,'INT' , 'STATIC'
        ,'PUBLIC' , 'NUMBER' , 'FOR' , 'PLUSPLUS', 'PRIVATE' , 'THIS' , 'DOUBLE' ,'CLASS', 'RETURN' , 'OPENAKOL' , 'CLOSEAKOL' , 'BOOLEAN' , 'DOT' ]



# List of  reserved tokens
reserved = {

    'while' : 'WHILE',
    'if' : 'IF',
    'for' : 'FOR',
    'switch' : 'SWITCH',
    'case' : 'CASE',
    'else' : 'ELSE',
    'do' : 'DO',
    'char' : 'CHARACTER',
    'int' : 'INT',
    'float' : 'FLOAT',
    'void'  : 'VOID',
    'boolean'  : 'BOOLEAN',
    'double' : 'DOUBLE',
    'return' : 'RETURN',
    'true'  : 'TRUE',
    'false' : 'FALSE',
    'null' : 'NULL',
    'new' : 'NEW',
    'static' : 'STATIC',
    'public' : 'PUBLIC',
    'private' : 'PRAIVATE',
    'this' : 'THIS',
    'class' : 'CLASS',
    'String' : 'STRING',
}


# Regular expression rules for simple tokens
t_NUMBER    = r'\d+'
t_LESSEQUAL = r'\<\='
t_ASSIGN    = r'\='
t_EQUALS    = r'\=\='
t_PLUSPLUS    = r'\+\+'
t_GREATEREQUAL = r'\>\='
t_NOTEQUAL  = r'\!\='
t_GREATERTHAN = r'\>'
t_LESSTHAN  = r'\<'
t_ADD       = r'\+'
t_MINUS     = r'\-'
t_MULT      = r'\*'
t_DIVIDE    = r'\/'
t_OPENPAR      = r'\('
t_CLOSEPAR  = r'\)'
t_OPENBRACKET = r'\['
t_CLOSEBRACKET = r'\]'
t_OPENAKOL = r'\{'
t_CLOSEAKOL= r'\}'
t_SEMI = r'\;'
t_PEQUAL = r'\+\='
t_MEQUAL    = r'\-\='
t_COMMA     = r'\,'
t_DOT = r'\.'


# A regular expression rule with some action code
def t_ID(t):
    r'[a-zA-Z_]+[0-9_]*'
    if t.value in reserved:
        t.type = reserved[ t.value ]
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

f = open("input2.txt","r")
data = f.readline()


# Give the lexer some input
lexer.input(data)

# Tokenize
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    print(tok)




##################################################################################################################
import ply.yacc as yacc


def p_programm(p):
    '''PROGRAM : Z'''

def p_Z(p):
    '''Z : CLASSDECLARATION Z
       Z : EMPTY'''

def p_classdeclaration(p):
    '''CLASSDECLARATION : CLASS ID OPENAKOL A CLOSEAKOL'''

def p_A(p):
    '''A : FIELDDECLARATION A
         | METHODDECLARATION A
         | EMPTY'''

def p_fielddeclaration(p):
    '''FIELDDECLARATION : DECLARATORS ID SEMI'''

def p_methoddeclaration(p):
    '''METHODDECLARATION : DECLARATORS ID OPENPAR PARAMERERLIST CLOSEPAR OPENAKOL B RETURN EXPRESSION SEMI CLOSEAKOL
       METHODDECLARATION : DECLARATORS ID OPENPAR CLOSEPAR OPENAKOL B RETURN EXPRESSION SEMI CLOSEAKOL
       METHODDECLARATION : DECLARATORS ID OPENPAR PARAMERERLIST CLOSEPAR OPENAKOL B CLOSEAKOL
       METHODDECLARATION : DECLARATORS ID OPENPAR  CLOSEPAR OPENAKOL B CLOSEAKOL'''


def p_B(p):
    '''B : STATEMENT B
         | EMPTY'''

def p_declarators(p):
    '''DECLARATORS : C STATIC TYPE
       DECLARATORS : STATIC TYPE
       DECLARATORS : C TYPE
       DECLARATORS : TYPE'''


def p_C(p):
    '''C : PUBLIC
       C : PRIVATE'''


def p_empty(p):
    '''EMPTY :'''

def p_type(p):
    '''TYPE : PRIMTYPE
       TYPE : CLASSTYPE
       TYPE : ARRTYPE'''

def p_primetype (p):
    '''PRIMTYPE : INT
       PRIMTYPE : BOOLEAN
       PRIMTYPE : STRING
       PRIMTYPE : DOUBLE
       PRIMTYPE : CHARACTER
       PRIMTYPE : FLOAT
       PRIMTYPE : VOID'''

def p_classtype(p):
    '''CLASSTYPE : ID '''

def p_arrtype(p):
    '''ARRTYPE : INT OPENBRACKET CLOSEBRACKET
       ARRTYPE : CLASSTYPE OPENBRACKET CLOSEBRACKET'''

def p_parameterlist(p):
    '''PARAMERERLIST : TYPE ID D'''

def p_D(p):
    '''D : COMMA TYPE ID D
       D : EMPTY'''

def p_argumentlist(p):
    '''ARGUMENTLIST : EXPRESSION E'''

def p_E(p):
    '''E : COMMA EXPRESSION
       E : EMPTY'''

def p_reference(p):
    '''REFERENCE : THIS G
       REFERENCE : ID G '''

def p_G(p):
    '''G : DOT ID G
       G : EMPTY'''

def p_statement (p):
    '''STATEMENT : OPENAKOL H CLOSEAKOL
       STATEMENT : TYPE ID ASSIGN EXPRESSION SEMI
       STATEMENT : REFERENCE OPENBRACKET EXPRESSION CLOSEBRACKET ASSIGN EXPRESSION SEMI
       STATEMENT : REFERENCE ASSIGN EXPRESSION SEMI
       STATEMENT : REFERENCE OPENPAR CLOSEPAR SEMI
       STATEMENT : REFERENCE OPENPAR ARGUMENTLIST CLOSEPAR SEMI
       STATEMENT : IF OPENPAR EXPRESSION CLOSEPAR STATEMENT ELSE STATEMENT
       STATEMENT : IF OPENPAR EXPRESSION CLOSEPAR STATEMENT
       STATEMENT : FOR OPENPAR EXPRESSION CLOSEPAR STATEMENT
       STATEMENT : WHILE OPENPAR EXPRESSION CLOSEPAR STATEMENT'''



def p_H (p):
    '''H : STATEMENT H
       H : EMPTY'''


def p_expressin (p):
    '''EXPRESSION : TRUE
       EXPRESSION : FALSE
       EXPRESSION : NULL
       EXPRESSION : NEW ID OPENPAR CLOSEPAR
       EXPRESSION : NEW INT OPENBRACKET EXPRESSION CLOSEBRACKET
       EXPRESSION : NEW ID OPENBRACKET EXPRESSION CLOSEBRACKET
       EXPRESSION : OPENPAR EXPRESSION CLOSEPAR
       EXPRESSION : EXPRESSION OP EXPRESSION
       EXPRESSION : EXPRESSION OP EXPRESSION SEMI
       EXPRESSION : NUMBER
       EXPRESSION : REFERENCE OPENPAR ARGUMENTLIST CLOSEPAR
       EXPRESSION : REFERENCE OPENPAR CLOSEPAR
       EXPRESSION : REFERENCE OPENBRACKET EXPRESSION CLOSEBRACKET
       EXPRESSION : REFERENCE
       EXPRESSION : REFERENCE ASSIGN REFERENCE SEMI REFERENCE OP REFERENCE SEMI I
       EXPRESSION : REFERENCE ASSIGN NUMBER SEMI REFERENCE OP NUMBER SEMI I
       EXPRESSION : REFERENCE ASSIGN NUMBER SEMI REFERENCE OP REFERENCE SEMI I'''

def p_op(p):
    '''OP : LESSEQUAL
          | ASSIGN
          | EQUALS
          | GREATEREQUAL
          | GREATERTHAN
          | LESSTHAN
          | ADD
          | MINUS
          | MULT
          | NOTEQUAL
          | DIVIDE
          | PEQUAL
          | MEQUAL
          | PLUSPLUS'''



def p_I(p):
    '''I : REFERENCE OP
       | REFERENCE OP NUMBER
       | REFERENCE OP REFERENCE'''

def p_error(p):
    print("syntax error!")
pars = yacc.yacc()

print("###########################")


pars.parse(data)
