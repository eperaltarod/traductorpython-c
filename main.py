from my_parser import parser
from lexer import lexer

# Leer el código desde input.py
with open('input.py', 'r') as file:
    code = file.read()

# Probar el parser
result = parser.parse(code, lexer=lexer)

# Escribir la salida en un archivo .c
with open('output.c', 'w') as output_file:
    output_file.write("#include <stdio.h>\n\n")
    output_file.write("int main() {\n")
    output_file.write(result)
    output_file.write("\n    return 0;\n")
    output_file.write("}\n")

print("Código traducido a C guardado en output.c")