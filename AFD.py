
from Token import Token
from Error import Error


class AFD:
    def __init__(self):
        self.tokens = []
        self.errores = []
        self.fila = 1
        self.columna = 1
        self.temporal = ''
        self.estado = 0
        self.simbolos = [";", ",", "=", "{", "}", "[", "]", "(", ")"]
        self.reservadas = ["CLAVES", "REGISTROS", "IMPRIMIR", "IMPRIMIRLN", "CONTEO", "PROMEDIO", "CONTARSI", "DATOS", "MAX", "MIN", "EXPORTARREPORTE", "SUMAR"]
        self.i = 0

    def analizador(self, cadena):
        self.tokens = []
        self.errores = []
        self.i = 0

        while self.i < len(cadena):
            if self.estado == 0:
                if cadena[self.i].isalpha():
                    self.temporal += cadena[self.i]
                    self.columna += 1
                    self.estado = 1
                
                elif cadena[self.i].isdigit():
                    self.temporal += cadena[self.i]
                    self.columna += 1
                    self.estado = 2

                elif cadena[self.i] in self.simbolos:
                    self.agregar_token(cadena[self.i], self.id_simbolos(cadena[self.i]))
                
                elif cadena[self.i] == '"':
                    self.temporal += cadena[self.i]
                    self.columna += 1
                    self.estado = 5

                elif cadena[self.i] == '#':
                    self.columna += 1
                    self.estado = 7

                elif cadena[self.i] == "'":
                    self.temporal += cadena[self.i]
                    self.columna += 1
                    self.estado = 9
                
                elif cadena[self.i] == '\n':
                    self.fila += 1
                    self.columna = 1

                elif cadena[self.i] in ['\t', ' ']:
                    self.columna += 1

                elif cadena[self.i] == '\r':
                    pass

                else:
                    self.temporal += cadena[self.i]
                    self.agregar_error(self.temporal)
                    self.columna += 1

            elif self.estado == 1:
                if cadena[self.i].isalnum():
                    self.temporal += cadena[self.i]
                    self.columna += 1
                else:
                    if self.temporal.upper() in self.reservadas:
                        self.agregar_token(self.temporal, self.temporal)
                        self.estado = 0
                        self.columna += 1
                        self.i -= 1
                    else:
                        self.agregar_error(self.temporal)
                        self.estado = 0
                        self.columna += 1
                        self.i -= 1

            elif self.estado == 2:
                if cadena[self.i].isdigit():
                    self.temporal += cadena[self.i]
                    self.columna += 1

                elif cadena[self.i] == ".":
                    self.temporal += cadena[self.i]
                    self.columna += 1
                    self.estado = 3

                else:
                    self.agregar_token(self.temporal, 'Entero')
                    self.estado = 0
                    self.columna += 1
                    self.i -= 1

            elif self.estado == 3:
                if cadena[self.i].isdigit():
                    self.temporal += cadena[self.i]
                    self.columna += 1
                else:
                    self.agregar_token(self.temporal, 'Decimal')
                    self.estado = 0
                    self.columna += 1
                    self.i -= 1
            
            elif self.estado == 5:
                if cadena[self.i] != '"':
                    self.temporal += cadena[self.i]
                    self.columna += 1
                else:
                    self.temporal += cadena[self.i]
                    self.agregar_token(self.temporal, 'Cadena')
                    self.estado = 0
                    self.columna += 1

            elif self.estado == 7:
                if cadena[self.i] == '\n':
                    self.estado = 0
                    self.fila += 1
                    self.columna = 1
                else:
                    self.columna += 1

            elif self.estado == 9:
                if cadena[self.i] == "'":
                    self.temporal += cadena[self.i]
                    self.estado = 10
                    self.columna += 1
                else:
                    self.agregar_error(self.temporal)
                    self.estado = 0
                    self.columna += 1
                    self.i -= 1

            elif self.estado == 10:
                if cadena[self.i] == "'":
                    self.temporal += cadena[self.i]
                    self.estado = 11
                    self.columna += 1
                else:
                    self.agregar_error(self.temporal)
                    self.estado = 0
                    self.columna += 1
                    self.i -= 1
            
            elif self.estado == 11:
                if cadena[self.i] == "'":
                    self.temporal += cadena[self.i]
                    self.estado = 12
                    self.columna += 1
                elif cadena[self.i] == '\n':
                    self.temporal += cadena[self.i]
                    self.fila += 1
                    self.columna = 1
                else:
                    self.temporal += cadena[self.i]
                    self.columna += 1
            
            elif self.estado == 12:
                if cadena[self.i] == "'":
                    self.temporal += cadena[self.i]
                    self.estado = 13
                    self.columna += 1
                else:
                    self.agregar_error(self.temporal)
                    self.estado = 0
                    self.columna += 1
                    self.i -= 1

            elif self.estado == 13:
                if cadena[self.i] == "'":
                    self.temporal = ""
                    self.estado = 0
                    self.columna += 1
                else:
                    self.agregar_error(self.temporal)
                    self.estado = 0
                    self.columna += 1
                    self.i -= 1

            self.i += 1
        return self.tokens, self.errores
#----------------------------------ag-----------
    def agregar_token(self, caracter, tipo):
        self.tokens.append(Token(caracter, tipo, self.fila, self.columna))
        self.temporal = ''

    def agregar_error(self, caracter):
        self.errores.append(Error(caracter, self.fila, self.columna))
        self.temporal = ''
#------------------------------------------------------------
#-----------------------imprimir----------------------------
    def imprimir_tokens(self):
        print("-" * 175)
        print("{:<50} {:<75} {:<55} {:<20}".format("Lexema", "Tipo", "Fila", "Columna"))
        print("-" * 175)
        for token in self.tokens:
            print("{:<50} {:<75} {:<55} {:<20}".format(token.lexema, token.tipo, token.fila, token.columna))

    def imprimir_errores(self):
        print("\nErrores:")
        print("{:<50} {:<55} {:<20}".format("Error", "Fila", "Columna"))
        print("-" * 125)
        for error in self.errores:
            print("{:<50} {:<55} {:<20}".format(error.descripcion, error.fila, error.columna))



#---------------------------------HTML-----------------------------------
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
#-------------------------------------------------

#agregar el simbolo que va a servir para el sintactico
    def id_simbolos(self, character):
        if character == ';':
            return "punto y coma"
        elif character == ',':
            return "Coma"
        elif character == '=':
            return "Igual"
        elif character == '{':
            return "Llave de apertura"
        elif character == '}':
            return "Llave de cierre"
        elif character == '[':
            return "Corchete de apertura"
        elif character == ']':
            return "Corchete de cierre"
        elif character == '(':
            return "Parentesis de apertura"
        elif character == ')':
            return "Parentesis de cierre"
        else:
            return "Símbolo"  # para que igual le asigne simbolo /////////// para que no de error 



#automata = AFD()
#with open('prueba_2.bizdata', 'r') as archivo:
    #contenido = archivo.read()

#resultado = automata.analizador(contenido)


#automata.imprimir_tokens()


#automata.imprimir_errores()
#automata.generate_tokens_table()


#automata.generate_errors_table()
