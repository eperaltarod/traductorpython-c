import ply.lex as lex

# Definición de los tokens
tokens = (
    'IDENTIFIER', 'NUMBER', 'ASSIGN', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'LPAREN', 'RPAREN', 'SEMICOLON', 'NEWLINE'
)

# Expresiones regulares para los tokens
t_ASSIGN = r'='
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_SEMICOLON = r';'
t_NEWLINE = r'\n'
t_IDENTIFIER = r'[a-zA-Z_][a-zA-Z0-9_]*'  # Identificadores como variables
t_NUMBER = r'\d+'  # Números enteros

# Regla para ignorar los espacios en blanco y tabulaciones
t_ignore = ' \t'

# Manejo de errores
def t_error(t):
    print(f"Caracter no reconocido: {t.value[0]}")
    t.lexer.skip(1)

# Crear el analizador léxico
lexer = lex.lex()