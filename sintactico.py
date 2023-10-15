from funciones import funciones
import  copy
#TIENE QUE RECIBIR LOS ERRORES Y LOS TOKESN DEL AFD LEXICO   

class sintactico:
    def __init__(self, tokens = [], errores_cf = []):
        self.errores_cf = errores_cf
        self.producto = []
        self.claves_datos = []
        self.funciones = funciones()
        self.ahora_t = ""
        self.start = ""
        self.tokens = tokens
        self.tokens.reverse()
        self.reservadas_lex = ["CLAVES", "REGISTROS", "IMPRIMIR", "IMPRIMIRLN", "CONTEO", "PROMEDIO", "CONTARSI", "DATOS", "MAX", "MIN", "EXPORTARREPORTE", "SUMAR", "PUNTO Y COMA"]


    def analizar_sintactico(self):
        self.Inicio_token()
        self.errores_html_stcs()
        return(self.ahora_t, self.errores_cf)
    
    #inicioa y mira si hay tokens y llama a la de funciones_rec
    def Inicio_token(self):
        if self.tokens:
            self.funciones_rec()


    def funciones_rec(self):
        self.funcion_def()
        self.funcion_seguir()

#SI NO ESTA EN LAS RESERVADAS SE PASA LAS SIGUIENTE >>< POP
    def funcion_seguir(self):
        try:
            temp = self.tokens[-1]
            while temp.tipo.upper() not in self.reservadas_lex:
                temp = self.tokens.pop()
        
            if temp.tipo.upper() in self.reservadas_lex:
                self.funcion_def()   #>>< MIRA LA FUNCION
                self.funcion_seguir() #RECURSIVIDAD PARA QUE CONTINUES
        except IndexError:
            pass
        except Exception as e:
            print("error en seguir >>>  no lo saco, no funcion no rec  ")
            pass


    def funcion_def(self):
        try:
            temp = self.tokens[-1]
            if temp.tipo == 'imprimir':
                self.imprimir_funcion()
            elif temp.tipo == 'Claves':
                self.definir_claves()
            elif temp.tipo == 'Registros':
                self.definir_registro()
            elif temp.tipo == 'imprimirln':
                self.imprimirln_funcion()
            elif temp.tipo == 'sumar':
                self.sumar_funcion()
            elif temp.tipo == 'max':
                self.max_funcion()
            elif temp.tipo == 'min':
                self.minimo_funcion()
            elif temp.tipo == 'conteo':
                self.conteo_funcion()
            elif temp.tipo == 'promedio':
                self.promedio_funcion()
            elif temp.tipo == 'contarsi':
                self.contar_si()
            elif temp.tipo == 'datos':
                self.datos_funcion()
            elif temp.tipo == 'exportarReporte':
                self.reporte_funcion_html()
            else:
                pass
        except IndexError:
            pass
        except Exception as e:
            print("error >>>> funcion_def")
            print(f"Error {e}")
            pass
    
    def imprimir_funcion(self):
        cadena = None
        temp = self.tokens.pop()

        if temp.tipo == "imprimir":
            printNd = temp.lexema
            temp = self.tokens.pop()

            if temp.tipo == "Parentesis de apertura":
                parentesisAp = temp.lexema
                temp = self.tokens.pop()

                if temp.tipo == "Cadena":
                    cadena = copy.deepcopy(temp.lexema)
                    cadena = cadena.replace('"', '')
                    self.ahora_t += cadena
                    cadenaLx = temp.lexema
                    temp = self.tokens.pop()

                    if temp.tipo == "Parentesis de cierre":
                        parentesisCi = temp.lexema
                        temp = self.tokens.pop()

                        if temp.tipo == "punto y coma":
                            print("si pasa")

                        else:
                            self.tokens.append(temp)
                            self.errores_sintacticos(temp.tipo, "punto y coma", temp.fila, temp.columna)
                    else:
                        self.tokens.append(temp)
                        self.errores_sintacticos(temp.tipo, "Parentesis de cierre", temp.fila, temp.columna)
                else:
                    self.tokens.append(temp)
                    self.errores_sintacticos(temp.tipo, "Cadena", temp.fila, temp.columna)
            else:
                self.tokens.append(temp)
                self.errores_sintacticos(temp.tipo, "Parentesis de apertura", temp.fila, temp.columna)
        else:
            self.tokens.append(temp)
            self.errores_sintacticos(temp.tipo, "imprimir", temp.fila, temp.columna)

    def imprimirln_funcion(self):
        cadena = None
        temp = self.tokens.pop()
        print("Normal")

        if temp.tipo == "imprimirln":
            printNd = temp.lexema
            temp = self.tokens.pop()

            if temp.tipo == "Parentesis de apertura":
                parentesisAp = temp.lexema
                temp = self.tokens.pop()

                if temp.tipo == "Cadena":
                    cadenaLx = copy.deepcopy(temp.lexema)
                    cadena = temp.lexema
                    cadena = cadena.replace('"', '')
                    self.ahora_t += "\n" + cadena
                    temp = self.tokens.pop()

                    if temp.tipo == "Parentesis de cierre":
                        parentesisCi = temp.lexema
                        temp = self.tokens.pop()

                        if temp.tipo == "punto y coma":
                            print("si")
                        else:
                            self.tokens.append(temp)
                            self.errores_sintacticos(temp.tipo, "punto y coma", temp.fila, temp.columna)
                            print("aca")
                    else:
                        self.tokens.append(temp)
                        self.errores_sintacticos(temp.tipo, "Parentesis de cierre", temp.fila, temp.columna)
                else:
                    self.tokens.append(temp)
                    self.errores_sintacticos(temp.tipo, "Cadena", temp.fila, temp.columna)
            else:
                self.tokens.append(temp)
                self.errores_sintacticos(temp.tipo, "Parentesis de apertura", temp.fila, temp.columna)
        else:
            self.tokens.append(temp)
            self.errores_sintacticos(temp.tipo, "imprimirln", temp.fila, temp.columna)

    def definir_claves(self):
        rowTemp = []
        temp = self.tokens.pop()
        
        if temp.tipo == "Claves":
            temp = self.tokens.pop()
            
            if temp.tipo == "Igual":
                temp = self.tokens.pop()

                if temp.tipo == "Corchete de apertura":
                    finish = False
                    while finish is False:
                        temp = self.tokens.pop()

                        if temp.tipo == "Cadena":
                            cadena = temp.lexema
                            cadena = cadena.replace('"', '')
                            rowTemp.append(cadena)
                            temp = self.tokens.pop()

                            if temp.tipo == "Coma":
                                continue
                            elif temp.tipo == "Corchete de cierre":
                                finish = True
                            else:
                                self.tokens.append(temp)
                                self.errores_sintacticos(temp.tipo, "punto y coma - Corchete de cierre", temp.fila, temp.columna)
                        else:
                            self.tokens.append(temp)
                            self.errores_sintacticos(temp.tipo, "Cadena", temp.fila, temp.columna)
                            break
                else:
                    self.tokens.append(temp)
                    self.errores_sintacticos(temp.tipo, "Corchete de apertura", temp.fila, temp.columna)
            else:
                self.tokens.append(temp)
                self.errores_sintacticos(temp.tipo, "Igual", temp.fila, temp.columna)
        else:
            self.tokens.append(temp)
            self.errores_sintacticos(temp.tipo, "Error", temp.fila, temp.columna)
        self.claves_datos = rowTemp
#crea los elemntos de los registros >>>> 
    def definir_registro(self):
        temp = self.tokens.pop()

        if temp.tipo == "Registros":
            temp = self.tokens.pop()

            if temp.tipo == "Igual":
                temp = self.tokens.pop()

                if temp.tipo == "Corchete de apertura":
                    records = True
                    while records:
                        temp = self.tokens.pop()

                        if temp.tipo == "Llave de apertura":
                            rowTemp = []
                            fin = False
                            while fin is False:
                                temp = self.tokens.pop()
                                
                                if temp.tipo == "Cadena" or temp.tipo == "Decimal" or temp.tipo == "Entero":
                                    cadena = temp.lexema
                                    cadena = cadena.replace('"', '')
                                    rowTemp.append(cadena)

                                    temp = self.tokens.pop()
                                    
                                    if temp.tipo == "Coma":
                                        continue
                                    elif temp.tipo == "Llave de cierre":
                                        fin = True
                                    else:
                                        self.tokens.append(temp)
                                        self.errores_sintacticos(temp.tipo, "Coma - Llave de cierre", temp.fila, temp.columna)
                                        break
                                else:
                                    self.tokens.append(temp)
                                    self.errores_sintacticos(temp.tipo, "Cadena", temp.fila, temp.columna)
                                    break
                            self.producto.append(rowTemp)

                        elif temp.tipo == "Corchete de cierre":
                            break
                        else:
                            self.tokens.append(temp)
                            self.errores_sintacticos(temp.tipo, "Llave de apertura - Corchete de cierre", temp.fila, temp.columna)
                    else:
                        self.tokens.append(temp)
                        self.errores_sintacticos(temp.tipo, "Corchete de apertura", temp.fila, temp.columna)
                else:
                    self.tokens.append(temp)
                    self.errores_sintacticos(temp.tipo, "Igual", temp.fila, temp.columna)
            else:
                self.tokens.append(temp)
                self.errores_sintacticos(temp.tipo, "Registros", temp.fila, temp.columna)

    def conteo_funcion(self):
        temp = self.tokens.pop()

        if temp.tipo == "conteo":
            count = temp.lexema
            temp = self.tokens.pop()

            if temp.tipo == "Parentesis de apertura":
                parentesisAp = temp.lexema
                temp = self.tokens.pop()

                if temp.tipo == "Parentesis de cierre":
                    parentesisCi = temp.lexema
                    temp = self.tokens.pop()
#contar todos los elementos de los registros >>>> fila/coluna
                    if temp.tipo == "punto y coma":
                        rows = len(self.producto)
                        columns = len(self.producto[0])
                        count = int(rows)*int(columns)
                        self.ahora_t += "\n>>>" + str(count)
                    
                    else:
                        self.tokens.append(temp)
                        self.errores_sintacticos(temp.tipo, "punto y coma", temp.fila, temp.columna)
                else:
                    self.tokens.append(temp)
                    self.errores_sintacticos(temp.tipo, "Parentesis de cierre", temp.fila, temp.columna)
            else:
                self.tokens.append(temp)
                self.errores_sintacticos(temp.tipo, "Parentesis de apertura", temp.fila, temp.columna)
        else:
            self.tokens.append(temp)
            self.errores_sintacticos(temp.tipo, "conteo", temp.fila, temp.columna)

    def promedio_funcion(self):
        cadena = None
        temp = self.tokens.pop()
        
        if temp.tipo == "promedio":
            average = temp.lexema
            temp = self.tokens.pop()

            if temp.tipo == "Parentesis de apertura":
                parentesisAp = temp.lexema
                temp = self.tokens.pop()

                if temp.tipo == "Cadena":
                    cadenaLx = temp.lexema
                    cadena = temp.lexema
                    temp = self.tokens.pop()

                    if temp.tipo == "Parentesis de cierre":
                        parentesisCi = temp.lexema
                        temp = self.tokens.pop()

                        if temp.tipo == "punto y coma":
                            res = self.funciones.promedio(self.producto, self.claves_datos, cadena)
                            print("<<<promedio calculado>>>")
                            if res is None:
                                print("Error")
                            else:
                                self.ahora_t += "\n>>>" + res

                        else:
                            self.tokens.append(temp)
                            self.errores_sintacticos(temp.tipo, "punto y coma", temp.fila, temp.columna)
                    else:
                        self.tokens.append(temp)
                        self.errores_sintacticos(temp.tipo, "Parentesis de cierre", temp.fila, temp.columna)
                else:
                    self.tokens.append(temp)
                    self.errores_sintacticos(temp.tipo, "Cadena", temp.fila, temp.columna)
            else:
                self.tokens.append(temp)
                self.errores_sintacticos(temp.tipo, "Parentesis de apertura", temp.fila, temp.columna)
        else:
            self.tokens.append(temp)
            self.errores_sintacticos(temp.tipo, "promedio", temp.fila, temp.columna)

    def contar_si(self):
        field = None
        value = None
        temp = self.tokens.pop()

        if temp.tipo == "contarsi":
            contarsi = temp.lexema
            temp = self.tokens.pop()

            if temp.tipo == "Parentesis de apertura":
                parentesisAp = temp.lexema
                temp = self.tokens.pop()

                if temp.tipo == "Cadena":
                    cadena1 = temp.lexema
                    field = temp.lexema
                    temp = self.tokens.pop()

                    if temp.tipo == "Coma":
                        comma = temp.lexema
                        temp = self.tokens.pop()                         

                        if temp.tipo == "Cadena" or temp.tipo == "Decimal" or temp.tipo == "Entero":
                            value = temp.lexema
                            cadena2 = temp.lexema
                            temp = self.tokens.pop()

                            if temp.tipo == "Parentesis de cierre":
                                parentesisCi = temp.lexema
                                temp = self.tokens.pop()

                                if temp.tipo == "punto y coma":
                                    res = self.funciones.contarSi(self.producto, self.claves_datos, field, value)
                                    print("si pudo contarlos >>>>>>>>>> ")
                                    if res is None:
                                        print("Error en contarSi")
                                    else:
                                        self.ahora_t += "\n>>>" + res
                                else:
                                    self.tokens.append(temp)
                                    self.errores_sintacticos(temp.tipo, "punto y coma", temp.fila, temp.columna)
                            else:
                                self.tokens.append(temp)
                                self.errores_sintacticos(temp.tipo, "Parentesis de cierre", temp.fila, temp.columna)
                        else:
                            self.tokens.append(temp)
                            self.errores_sintacticos(temp.tipo, "Cadena - Decimal - Entero", temp.fila, temp.columna)
                    else:
                        self.tokens.append(temp)
                        self.errores_sintacticos(temp.tipo, "Coma", temp.fila, temp.columna)
                else:
                    self.tokens.append(temp)
                    self.errores_sintacticos(temp.tipo, "Cadena", temp.fila, temp.columna)
            else:
                self.tokens.append(temp)
                self.errores_sintacticos(temp.tipo, "Parentesis de apertura", temp.fila, temp.columna)
        else:
            self.tokens.append(temp)
            self.errores_sintacticos(temp.tipo, "contarsi", temp.fila, temp.columna)

    def datos_funcion(self):
        temp = self.tokens.pop()

        if temp.tipo == "datos":
            data = temp.lexema
            temp = self.tokens.pop()

            if temp.tipo == "Parentesis de apertura":
                parentesisAp = temp.lexema
                temp = self.tokens.pop()

                if temp.tipo == "Parentesis de cierre":
                    parentesisCi = temp.lexema
                    temp = self.tokens.pop()

                    if temp.tipo == "punto y coma":
                        self.impTabla()
                        #ACA SE IMPRIME
                        print(">>>>>>>tabla impresa<<<<<<<")
                        pass
                    else:
                        self.tokens.append(temp)
                        self.errores_sintacticos(temp.tipo, "punto y coma", temp.fila, temp.columna)
                else:
                    self.tokens.append(temp)
                    self.errores_sintacticos(temp.tipo, "Parentesis de cierre", temp.fila, temp.columna)
            else:
                self.tokens.append(temp)
                self.errores_sintacticos(temp.tipo, "Parénteisis de apertura", temp.fila, temp.columna)
        else:
            self.tokens.append(temp)
            self.errores_sintacticos(temp.tipo, "datos", temp.fila, temp.columna)

    def sumar_funcion(self):
        cadena = None
        temp = self.tokens.pop()

        if temp.tipo == "sumar":
            sum = temp.lexema
            temp = self.tokens.pop()

            if temp.tipo == "Parentesis de apertura":
                parentesisAp = temp.lexema
                temp = self.tokens.pop()

                if temp.tipo == "Cadena":
                    cadenaLx = temp.lexema
                    cadena = temp.lexema
                    temp = self.tokens.pop()

                    if temp.tipo == "Parentesis de cierre":
                        parentesisCi = temp.lexema
                        temp = self.tokens.pop()

                        if temp.tipo == "punto y coma":
                            res = self.funciones.sumar(self.producto, self.claves_datos, cadena)
                            print("SUMMMMMAAAAAAAA")
                            if res is None:
                                print("Error en SUMA")
                            else:
                                self.ahora_t += "\n>>>" + res
                        else:
                            self.tokens.append(temp)
                            self.errores_sintacticos(temp.tipo, "punto y coma", temp.fila, temp.columna)
                    else:
                        self.tokens.append(temp)
                        self.errores_sintacticos(temp.tipo, "Parentesis de cierre", temp.fila, temp.columna)
                else:
                    self.tokens.append(temp)
                    self.errores_sintacticos(temp.tipo, "Cadena", temp.fila, temp.columna)
            else:
                self.tokens.append(temp)
                self.errores_sintacticos(temp.tipo, "Parentesis de apertura", temp.fila, temp.columna)
        else:
            self.tokens.append(temp)
            self.errores_sintacticos(temp.tipo, "sumar", temp.fila, temp.columna)
    
    def max_funcion(self):
        cadena = None
        temp = self.tokens.pop()

        if temp.tipo == "max":
            maximum = temp.lexema
            temp = self.tokens.pop()

            if temp.tipo == "Parentesis de apertura":
                parentesisAp = temp.lexema
                temp = self.tokens.pop()

                if temp.tipo == "Cadena":
                    cadenaLx = temp.lexema
                    cadena = temp.lexema
                    temp = self.tokens.pop()

                    if temp.tipo == "Parentesis de cierre":
                        parentesisCi = temp.lexema
                        temp = self.tokens.pop()

                        if temp.tipo == "punto y coma":
                            res = self.funciones.max(self.producto, self.claves_datos, cadena)
                            print("maximo funciona")
                            if res is None:
                                print("Error en max")
                            else:
                                self.ahora_t += "\n>>>" + res
                        else:
                            self.tokens.append(temp)
                            self.errores_sintacticos(temp.tipo, "punto y coma", temp.fila, temp.columna)
                    else:
                        self.tokens.append(temp)
                        self.errores_sintacticos(temp.tipo, "Parentesis de cierre", temp.fila, temp.columna)
                else:
                    self.tokens.append(temp)
                    self.errores_sintacticos(temp.tipo, "Cadena", temp.fila, temp.columna)
            else:
                self.tokens.append(temp)
                self.errores_sintacticos(temp.tipo, "Parentesis de apertura", temp.fila, temp.columna)
        else:
            self.tokens.append(temp)
            self.errores_sintacticos(temp.tipo, "max", temp.fila, temp.columna)

    def minimo_funcion(self):
        cadena = None
        temp = self.tokens.pop()
        if temp.tipo == "min":
            minimum = temp.lexema
            temp = self.tokens.pop()

            if temp.tipo == "Parentesis de apertura":
                parentesisAp = temp.lexema
                temp = self.tokens.pop()

                if temp.tipo == "Cadena":
                    cadenaLx = temp.lexema
                    cadena = temp.lexema
                    temp = self.tokens.pop()

                    if temp.tipo == "Parentesis de cierre":
                        parentesisCi = temp.lexema
                        temp = self.tokens.pop()

                        if temp.tipo == "punto y coma":
                            res = self.funciones.min(self.producto, self.claves_datos, cadena)
                            print("minimo funciona")
                            if res is None:
                                print("Error en min")
                            else:
                                self.ahora_t += "\n>>>" + res
                        else:
                            self.tokens.append(temp)
                            self.errores_sintacticos(temp.tipo, "punto y coma", temp.fila, temp.columna)
                    else:
                        self.tokens.append(temp)
                        self.errores_sintacticos(temp.tipo, "Parentesis de cierre", temp.fila, temp.columna)
                else:
                    self.tokens.append(temp)
                    self.errores_sintacticos(temp.tipo, "Cadena", temp.fila, temp.columna)
            else:
                self.tokens.append(temp)
                self.errores_sintacticos(temp.tipo, "Parentesis de apertura", temp.fila, temp.columna)
        else:
            self.tokens.append(temp)
            self.errores_sintacticos(temp.tipo, "min", temp.fila, temp.columna)
#--------------------

    def errores_sintacticos(self, el_error, exp, fila, columna):
        self.errores_cf.append(
            "<sintactico> token: '{}'>>>>>> '{}'. [Fila: {}, Columna: {}]".format(el_error,exp,fila,columna) )
        temp = self.tokens[-1]
        while temp.tipo.upper() not in self.reservadas_lex:
            temp = self.tokens.pop()

#--------------------------------- reporte ?
    def reporte_funcion_html(self):
        cadena = None
        temp = self.tokens.pop()

        if temp.tipo == "exportarReporte":
            report = temp.lexema
            temp = self.tokens.pop()

            if temp.tipo == "Parentesis de apertura":
                parentesisAp = temp.lexema
                temp = self.tokens.pop()

                if temp.tipo == "Cadena":
                    cadena = temp.lexema
                    cadenaLx = temp.lexema
                    temp = self.tokens.pop()

                    if temp.tipo == "Parentesis de cierre":
                        parentesisCi = temp.lexema
                        temp = self.tokens.pop()
                        if temp.tipo == "punto y coma":
                            self.reporteHTML(cadena)
                            print("REPORTEEEEEE")
                        else:
                            self.tokens.append(temp)
                            self.errores_sintacticos(temp.tipo, "punto y coma", temp.fila, temp.columna)
                    else:
                        self.tokens.append(temp)
                        self.errores_sintacticos(temp.tipo, "Parentesis de cierre", temp.fila, temp.columna)
                else:
                    self.tokens.append(temp)
                    self.errores_sintacticos(temp.tipo, "Cadena", temp.fila, temp.columna)
            else:
                self.tokens.append(temp)
                self.errores_sintacticos(temp.tipo, "Parentesis de apertura", temp.fila, temp.columna)
        else:
            self.tokens.append(temp)
            self.errores_sintacticos(temp.tipo, "exportarReporte", temp.fila, temp.columna)
    
    def impTabla(self):
        if len(self.producto) == 0:
            print('No hay valores en la tabla.')
        else:
            max_lengths = [max(len(str(value)) for value in fila) for fila in zip(*self.producto)]
            row_format = ' '.join(['{{:<{}}}'.format(length) for length in max_lengths])
            separator = '*' * (sum(max_lengths) + len(max_lengths) - 1)  

        
            print(row_format.format(*self.claves_datos))
            print(separator)

        
            for fila in self.producto:
                print(row_format.format(*fila))

            self.ahora_t += "\n" + ' '.join(map(str, self.claves_datos)) + "\n" + separator + "\n" + '\n'.join([' '.join(map(str, fila)) for fila in self.producto])


#------------------------------------------ ERRORES Y REPORTE --- HTML ---------------

    def errores_html_stcs(self, filename="tabla_de_errores.html"):
        if len(self.errores_cf) == 0:
            print('No hay errores en la lista.')
        else:
        
            html_table = '<table style="background-color: lightpink;">'
            html_table += '<tr><th>Errores</th></tr>'
        
            for value in self.errores_cf:
                html_table += f'<tr><td>{value}</td></tr>'
        
            html_table += '</table>'

        
            with open(filename, 'w') as file:
                file.write(html_table)

            print(f'HTML de errores creado >>>> {filename}')

    def reporteHTML(self, header):
        if len(self.producto) == 0:
            print('No hay valores en la tabla.')
        else:
            max_lengths = [max(len(str(value)) for value in fila) for fila in zip(*self.producto)]
            row_format = ' '.join(['{{:<{}}}'.format(length) for length in max_lengths])

            html_content = f"""<html>\n<head>
                <style>
                    table {{
                        font-family: arial, sans-serif;
                        border-collapse: collapse;
                        width: 100%;
                    }}
                    th, td {{
                        border: 1px solid #dddddd;
                        text-align: left;
                        padding: 8px;
                    }}
                    tr:nth-child(even) {{
                        background-color: #f2f2f2;
                    }}
                    th {{
                        background-color: #aebcea;
                    }}
                </style>
            </head>\n<body>\n<table>\n<tr><th colspan='{len(self.claves_datos)}'>{header}</th></tr>\n
            </head>\n<body>\n<table>\n<tr><th>{'</th><th>'.join(map(str, self.claves_datos))}</th></tr>\n"""

            for fila in self.producto:
                html_content += "<tr>" + ''.join([f"<td>{val}</td>" for val in fila]) + "</tr>\n"

            html_content += "</table>\n</body>\n</html>"

            with open('Reporte_registros.html', 'w') as file:
                file.write(html_content)

