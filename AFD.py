from Error import Error
from Token import Token

class AFD:
    def __init__(self):
        self.tokens = []
        self.errores = []
        self.fila = 1
        self.columna = 1
        self.temporal = ''
        self.estado = 0
        self.simbolos = [";", ",", "=", "{", "}", "[", "]", "(", ")"]
        self.reservadas = ["claves", "Registros", "imprimir", "imprimirln", "conteo", "promedio", "contarsi", "datos", "max", "min", "exportarReporte", "sumar"]

    def agregar_token(self, caracter, tipo):
        self.tokens.append(Token(caracter, tipo, self.fila, self.columna))
        self.temporal = ''

    def agregar_error(self, caracter):
        self.errores.append(Error(caracter, self.fila, self.columna))
        self.temporal = ''

    def analizador(self, cadena):
        self.tokens = []
        self.errores = []
        in_triple_quote = False
        i = 0


        while i < len(cadena):
            if self.estado == 0:
                if cadena[i].isalpha():
                    self.temporal += cadena[i]
                    self.columna += 1
                    self.estado = 1
                
                elif cadena[i].isdigit():
                    self.temporal += cadena[i]
                    self.columna += 1
                    self.estado = 2

                elif cadena[i] in self.simbolos:
                    self.agregar_token(str(cadena[i]), "Símbolo")
                
                elif cadena[i] == '"':
                    self.temporal += cadena[i]
                    self.columna += 1
                    self.estado = 5

                elif cadena[i] == '#':
                    self.columna += 1
                    self.estado = 7

                elif cadena[i] == "'":
                    self.temporal += cadena[i]
                    self.columna += 1
                    self.estado = 9
                
                elif cadena[i] == '\n':
                    self.fila += 1
                    self.columna = 1

                elif cadena[i] == '\r':
                    pass
                elif cadena[i] == " ":
                    self.columna += 1

                elif cadena[i] == "\t":
                    self.columna += 1

                elif cadena[i:i+3] == '"""':
                    if in_triple_quote:
                        in_triple_quote = False
                        self.columna += 3
                        i += 2
                    else:
                        in_triple_quote = True
                        self.columna += 3
                        i += 2
                    self.estado = 6

                else:
                    self.temporal += cadena[i]
                    self.agregar_error(self.temporal)
                    self.columna += 1
                    
            elif self.estado == 1:
                if cadena[i].isalnum():
                    self.temporal += cadena[i]
                    self.columna += 1
                else:
                    if self.temporal in self.reservadas:
                        self.agregar_token(self.temporal.strip(), "Reservada")
                        self.estado = 0
                        self.columna += 1
                        i -=1
                    else:
                        self.agregar_error(self.temporal)
                        self.estado = 0
                        self.columna += 1
                        i -= 1

            elif self.estado == 2:
                if cadena[i].isdigit():
                    self.temporal += cadena[i]
                    self.columna += 1

                elif cadena[i] == ".":
                    self.temporal += cadena[i]
                    self.columna += 1
                    self.estado = 3

                else:
                    self.agregar_token(self.temporal, 'Entero')
                    self.estado = 0
                    self.columna += 1
                    i -= 1

            elif self.estado == 3:
                if cadena[i].isdigit():
                    self.temporal += cadena[i]
                    self.columna += 1
                else:
                    self.agregar_token(self.temporal, 'Decimal')
                    self.estado = 0
                    self.columna += 1
                    i -= 1
            
            elif self.estado == 5:
                if cadena[i] != "\"":
                    self.temporal += cadena[i]
                    self.columna += 1
                else:
                    self.temporal += cadena[i]
                    self.agregar_token(self.temporal, "Cadena")
                    self.estado = 0
                    self.columna += 1

            elif self.estado == 6:
                
                if cadena[i:i+3] == '"""':
                    in_triple_quote = False
                    self.columna += 3
                    i += 2
                    self.temporal = ''
                else:
                    self.temporal += cadena[i]
                    self.columna += 1
                    self.estado = 5

            elif self.estado == 7:
                if cadena[i] == '\n':
                    self.estado = 0
                    self.fila += 1
                    self.columna = 1
                else:
                    self.columna += 1

            elif self.estado == 9:
                if cadena[i] == "'":
                    self.temporal += cadena[i]
                    self.estado = 10
                    self.columna += 1
                else:
                    self.agregar_error(self.temporal)
                    self.estado = 0
                    self.columna += 1
                    i -= 1

            elif self.estado == 10:
                if cadena[i] == "'":
                    self.temporal += cadena[i]
                    self.estado = 11
                    self.columna += 1
                else:
                    self.agregar_error(self.temporal)
                    self.estado = 0
                    self.columna += 1
                    i -= 1
            
            elif self.estado == 11:
                if cadena[i] == "'":
                    self.temporal += cadena[i]
                    self.estado = 12
                    self.columna += 1
                elif cadena[i] == '\n':
                    self.temporal += cadena[i]
                    self.fila += 1
                    self.columna = 1
                else:
                    self.temporal += cadena[i]
                    self.columna += 1
            
            elif self.estado == 12:
                if cadena[i] == "'":
                    self.temporal += cadena[i]
                    self.estado = 13
                    self.columna += 1
                else:
                    self.agregar_error(self.temporal)
                    self.estado = 0
                    self.columna += 1
                    i -= 1

            elif self.estado == 13:
                if cadena[i] == "'":
                    self.temporal = ""
                    self.estado = 0
                    self.columna += 1
                else:
                    self.agregar_error(self.temporal)
                    self.estado = 0
                    self.columna += 1
                    i -= 1
            i += 1
        return self.tokens, self.errores

    def imprimir_tokens(self):
        print("Tokens:")
        print("{:<25} {:<15} {:<10} {:<10}".format("Lexema", "Tipo", "Fila", "Columna"))
        print("-" * 65)
        for token in self.tokens:
            print("{:<25} {:<15} {:<10} {:<10}".format(token.lexema, token.tipo, token.fila, token.columna))

    def imprimir_errores(self):
        print("\nErrores:")
        print("{:<30} {:<10} {:<10}".format("Error", "Fila", "Columna"))
        print("-" * 45)
        for error in self.errores:
            print("{:<30} {:<10} {:<10}".format(error.descripcion, error.fila, error.columna))

    def generate_reporte_html(self, data, headers, filename, table_color):
        table_html = f'<table border="1" style="background-color: {table_color};">\n'
        table_html += '<tr>'
        for header in headers:
            table_html += f'<th>{header}</th>'
        table_html += '</tr>\n'
        for row in data:
            table_html += '<tr>'
            for cell in row:
                table_html += f'<td>{cell}</td>'
            table_html += '</tr>\n'
        table_html += '</table>'
        
        with open(filename, 'w') as html_file:
            html_file.write('<html>\n<head><title>REPORTE</title></head>\n<body>\n')
            html_file.write(table_html)
            html_file.write('</body>\n</html>')

    def generate_tokens_reporte(self):
        
        tokens_data = [[token.lexema, token.tipo, token.fila, token.columna] for token in self.tokens]
        tokens_headers = ["Lexema", "Tipo", "Fila", "Columna"]
        self.generate_reporte_html(tokens_data, tokens_headers, 'tokens_reporte.html', 'lightyellow')

    def generate_errors_reporte(self):
        
        errors_data = [[error.descripcion, error.fila, error.columna] for error in self.errores]
        errors_headers = ["Error", "Fila", "Columna"]
        self.generate_reporte_html(errors_data, errors_headers, 'errores_reporte.html', 'lightgreen')




#automata = AFD()
#with open('prueba_2.bizdata', 'r') as archivo:
    #contenido = archivo.read()

#resultado = automata.analizador(contenido)


#automata.imprimir_tokens()


#automata.imprimir_errores()
#automata.generate_tokens_table()


#automata.generate_errors_table()
