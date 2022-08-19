import ply.lex as lex


# List of token names.   This is always required
tokens = [ 'ID', 'LESSEQUAL','GREATEREQUAL', 'ASSIGN','EQUALS','NOTEQUAL',
        'GREATERTHAN','LESSTHAN','ADD','MINUS','MULT','DIVIDE','OPENPAR','CLOSEPAR','OPENBRACKET'
        ,'CLOSEBRACKET','SEMI','PEQUAL','MEQUAL','FLOAT','WHILE','IF','ELSE','CHARACTER','VOID','COMMA','TRUE','FALSE','NULL' , 'NEW' ,'STRING' ,'INT' , 'STATIC'
        ,'PUBLIC' , 'NUMBER' , 'FOR' , 'PLUSPLUS', 'PRIVATE' , 'THIS' , 'DOUBLE' ,'CLASS', 'RETURN' , 'OPENAKOL' , 'CLOSEAKOL' , 'BOOLEAN' , 'DOT' , 'CHAR' ]



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
t_CHAR = r'\'[a-zA-Z]\''


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

data = '''
class MyClass  {
public static void main(){
char a;
char b;
int z = a + b;
int z = 10;
k = m - c;
int f;
int w;
w = 'a' ;
f = h * i;
int m = l / k;

}
}
'''





# Give the lexer some input
#lexer.input(data)

# Tokenize
#while True:
#    tok = lexer.token()
#    if not tok:
#        break  # No more input
#    print(tok)




##################################################################################################################
import ply.yacc as yacc


symbol_table = {}
in_code = []
errors = []
results = []


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
    '''FIELDDECLARATION : DECLARATORS ID SEMI
       FIELDDECLARATION : STATEMENT'''


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
    p[0]= p[1]


def p_C(p):
    '''C : PUBLIC
       C : PRIVATE'''
    p[0]=p[1]


def p_empty(p):
    '''EMPTY :'''


def p_type(p):
    '''TYPE : PRIMTYPE
       TYPE : CLASSTYPE
       TYPE : ARRTYPE'''
    p[0] = p[1]

def p_primetype (p):
    '''PRIMTYPE : INT
       PRIMTYPE : BOOLEAN
       PRIMTYPE : STRING
       PRIMTYPE : DOUBLE
       PRIMTYPE : CHARACTER
       PRIMTYPE : FLOAT
       PRIMTYPE : VOID'''
    p[0]=p[1]


def p_classtype(p):
    '''CLASSTYPE : ID '''
    p[0]=p[1]

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
       STATEMENT : EXPRESSION
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
    '''EXPRESSION : EXPRESSION1
                  | EXPRESSION2
                  | EXPRESSION3
                  | EXPRESSION4
                  | EXPRESSION5
                  | EXPRESSION6'''

def p_expressin1 (p):
    '''EXPRESSION1 : ID ASSIGN ID OP ID SEMI'''

    if p[1] not in symbol_table.keys():
        errors.append("Variable ("+p[1]+") is not defined !!!")

    if p[3] not in symbol_table.keys():
        errors.append("Variable ("+p[3]+") is not defined !!!")

    if p[5] not in symbol_table.keys():
        errors.append("Variable ("+p[5]+") is not defined !!!")

    elif (p[1] in symbol_table.keys() and p[3] in symbol_table.keys() and p[5] in symbol_table.keys()) and  (symbol_table.__getitem__(p[3]) != symbol_table.__getitem__(p[1]) or symbol_table.__getitem__(p[5]) != symbol_table.__getitem__(p[1]) ):
        errors.append("Cannot assign variables with different types !!! ("+p[1]+") != ("+p[3]+","+p[5]+")")

    if p[4] == '+':
        p[0] = '(' + p[4] + ',' + p[3] + ',' + p[5] + ',' + p[1] + ')'
        print(p[0])

    elif p[4] == '-':
        p[0] = '(' + p[4] + ',' + p[3] + ',' + p[5] + ',' + p[1] + ')'
        print(p[0])

    elif p[4] == '-':
        p[0] = '(' + p[4] + ',' + p[3] + ',' + p[5] + ',' + p[1] + ')'
        print(p[0])

    elif p[4] == '*':
        p[0] = '(' + p[4] + ',' + p[3] + ',' + p[5] + ',' + p[1] + ')'
        print(p[0])



def p_expressin2 (p):
    '''EXPRESSION2 : TYPE ID ASSIGN ID OP ID SEMI'''

    if p[2] not in symbol_table.keys():
        symbol_table.__setitem__(p[2], p[1])
    elif p[2] in symbol_table.keys():
        errors.append("Variable ("+p[2]+") is already defined by this name!!!")

    if p[4] not in symbol_table.keys():
        errors.append("Variable (" + p[4] + ") is not defined !!!")

    if p[6] not in symbol_table.keys():
        errors.append("Variable (" + p[6] + ") is not defined !!!")

    elif (p[4] in symbol_table.keys() and p[6] in symbol_table.keys()) and (
            symbol_table.__getitem__(p[4]) != p[1] or symbol_table.__getitem__(
            p[6]) != p[1]):
        errors.append("Cannot assign variables with different types !!! ("+p[2]+") != ("+p[4]+","+p[6]+")")

    if p[5] == '+':
        p[0] = '(' + p[5] + ',' + p[4] + ',' + p[6] + ',' + p[2] + ')'
        print(p[0])

    elif p[5] == '-':
        p[0] = '(' + p[5] + ',' + p[4] + ',' + p[6] + ',' + p[2] + ')'
        print(p[0])

    elif p[5] == '/':
        p[0] = '(' + p[5] + ',' + p[4] + ',' + p[6] + ',' + p[2] + ')'
        print(p[0])

    elif p[5] == '*':
        p[0] = '(' + p[5] + ',' + p[4] + ',' + p[6] + ',' + p[2] + ')'
        print(p[0])


def p_expressin3 (p):
    '''EXPRESSION3 : TYPE ID SEMI'''

    if p[2] not in symbol_table.keys():
        symbol_table.__setitem__(p[2], p[1])
    elif p[2] in symbol_table.keys():
        errors.append("Variable ("+p[2]+") is already defined by this name!!!")

def p_expressin4 (p):
    '''EXPRESSION4 : TYPE ID ASSIGN VALUE SEMI'''

    if p[2] not in symbol_table.keys():
        symbol_table.__setitem__(p[2], p[1])
    elif p[2] in symbol_table.keys():
        errors.append("Variable ("+p[2]+") is already defined by this name!!!")

    if (symbol_table.get(p[1]) == 'int' and p[4] == 'false'):
        errors.append("WRONG ASSIGNMENT!!! Type of Variable ("+p[2]+") is 'int' but Value is char!")
    if (symbol_table.get(p[1]) == 'char' and p[4] == 'true'):
        errors.append("WRONG ASSIGNMENT!!! Type of Variable ("+p[2]+") is 'char' but Value is int!")


def p_expressin5 (p):
    '''EXPRESSION5 : ID ASSIGN VALUE SEMI'''

    if p[1] not in symbol_table.keys():
        errors.append("Variable ("+p[1]+") is not defined !!!")

    if (symbol_table.get(p[1]) == 'int' and p[3] == 'false'):
        errors.append("WRONG ASSIGNMENT!!! Type of Variable ("+p[1]+") is 'int' but Value is char!")

    if (symbol_table.get(p[1]) == 'char' and p[3] == 'true'):
        errors.append("WRONG ASSIGNMENT!!! Type of Variable ("+p[1]+") is 'char' but Value is int!")



def p_value (p):
    '''VALUE : VALUE1
             | VALUE2'''
    p[0] = p[1]

def p_value1 (p):
    '''VALUE1 : NUMBER'''
    p[0] = 'true'

def p_value2 (p):
    '''VALUE2 : CHAR'''
    p[0] = 'false'


def p_expressin6 (p):
    '''EXPRESSION6 : TRUE
       EXPRESSION6 : FALSE
       EXPRESSION6 : NULL
       EXPRESSION6 : ID
       EXPRESSION6 : VALUE
       EXPRESSION6 : TYPE ID ASSIGN EXPRESSION OP EXPRESSION SEMI
       EXPRESSION6 : ID ASSIGN ID OP ID OP ID SEMI
       EXPRESSION6 : EMPTY
       EXPRESSION6 : REFERENCE ASSIGN NUMBER SEMI REFERENCE OP REFERENCE SEMI I'''

    p[0] = p[1]


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
    p[0] = p[1]



def p_I(p):
    '''I : REFERENCE OP
       | REFERENCE OP NUMBER
       | REFERENCE OP REFERENCE'''

# Error rule for syntax errors
def p_error(p):
    errors.append("Syntax error in input!!! at line: %s "%(p.lineno))

pars = yacc.yacc()


print("###########################")
lexer.lineno = 0
pars.parse(data)
i = 0
print("\nERRORS: ")
for i in errors:
    print(i)

print("\n###########\nSYMBOL TABLE: ",symbol_table)