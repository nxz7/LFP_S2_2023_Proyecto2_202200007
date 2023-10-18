class funciones:
    #CAMPO EL VALOR DE LAS CLAVES ()
    def contarSi(self, registros, claves, campo, valor):
        cadena = campo.replace('"', '')
        conteo = 0
        largo = len(registros)
#CLAVES >>> EL VALOR ESPECIFICO QUE SE VA A CONTAR, itera y va aumentando el valor 
        for val in claves:
            if str(val) == str(cadena):
                suma = 0
                i = 0
                while largo > i:
                    if registros[i][conteo] == str(valor).replace('"', ''):
                        suma += 1
                    i += 1
                return str(suma)
            conteo += 1
        return None

    def max(self, registros, claves, campo):
        cadena = campo.replace('"', '')
        conteo = 0
        maximo = 0
        largo = len(registros)
#itera 
        for valor in claves:
            if valor == cadena:
                i = 0
                #va actualizando el valor si es uno maximo
                while largo > i:
                    if float(registros[i][conteo]) > maximo:
                        maximo = float(registros[i][conteo])
                    i += 1
                return str(maximo)
            conteo += 1
        return None

    def min(self, registros, claves, campo):
        cadena = campo.replace('"', '')
        conteo = 0
        minimo = float('inf')
        largo = len(registros)

        for valor in claves:
            if valor == cadena:
                i = 0
                while largo > i:
                    if float(registros[i][conteo]) < minimo:
                        minimo = float(registros[i][conteo])
                    i += 1
                return str(minimo)
            conteo += 1
        return None

    def promedio(self, registros, claves, campo):
        cadena = campo.replace('"', '')
        conteo = 0
        largo = len(registros)

        for valor in claves:
            if valor == cadena:
                #sumando de acuerdo al campo y luego divide i
                suma = 0
                i = 0
                while largo > i:
                    suma += float(registros[i][conteo])
                    i += 1
                total = float(suma) / float(i)
                return str(round(total, 2))
            conteo += 1
        return None

    def sumar(self, registros, claves, campo):
        cadena = campo.replace('"', '')
        conteo = 0
        largo = len(registros)

        for valor in claves:
            if valor == cadena:
                suma = 0
                i = 0
                while largo > i:
                    suma += float(registros[i][conteo])
                    i += 1
                return str(round(suma, 2))
            conteo += 1
        return None
