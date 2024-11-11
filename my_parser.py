import ply.yacc as yacc
from lexer import tokens, lexer  # Importar la lista de tokens y el lexer

# Regla principal que permite múltiples declaraciones
def p_statements(p):
    '''statements : statements statement
                  | statement'''
    if len(p) == 3:
        p[0] = p[1] + '\n' + p[2]
    else:
        p[0] = p[1]

# Regla para manejar asignaciones
def p_statement_assign(p):
    'statement : IDENTIFIER ASSIGN expression SEMICOLON'
    p[0] = f"int {p[1]} = {p[3]};"

# Regla para manejar expresiones con números
def p_expression_number(p):
    'expression : NUMBER'
    p[0] = p[1]

# Regla para manejar identificadores
def p_expression_identifier(p):
    'expression : IDENTIFIER'
    p[0] = p[1]

# Regla para operaciones binarias
def p_expression_binop(p):
    '''expression : expression PLUS expression
                  | expression MINUS expression
                  | expression TIMES expression
                  | expression DIVIDE expression'''
    if p[2] == '+':
        p[0] = f"({p[1]} + {p[3]})"
    elif p[2] == '-':
        p[0] = f"({p[1]} - {p[3]})"
    elif p[2] == '*':
        p[0] = f"({p[1]} * {p[3]})"
    elif p[2] == '/':
        p[0] = f"({p[1]} / {p[3]})"

# Regla para manejar líneas nuevas
def p_statement_newline(p):
    'statement : NEWLINE'
    p[0] = ''

# Manejo de errores de sintaxis
def p_error(p):
    if p:
        print(f"Error de sintaxis en: {p}")
    else:
        print("Error de sintaxis en EOF")

# Crear el parser
parser = yacc.yacc()