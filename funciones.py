class funciones:
    def contarSi(self, records, keys, field, value):
        cadena = field.replace('"', '')
        count = 0
        large = len(records)

        for val in keys:
            if str(val) == str(cadena):
                suma = 0
                i = 0
                while large>i:
                    if records[i][count] == str(value).replace('"', ''):
                        suma += 1
                    i += 1
                return str(suma)
            count += 1
        return None
    
    def max(self, records, keys, field):
        cadena = field.replace('"', '')
        count = 0
        max = 0
        large = len(records)

        for value in keys:
            if value == cadena:
                i = 0
                while large>i:
                    if float(records[i][count]) > max:
                        max = float(records[i][count])
                    i += 1
                return str(max)
            count += 1
        return None         

    def min(self, records, keys, field):
        cadena = field.replace('"', '')
        count = 0
        min = float('inf')
        large = len(records)

        for value in keys:
            if value == cadena:
                i = 0
                while large>i:
                    if float(records[i][count]) < min:
                        min = float(records[i][count])
                    i += 1
                return str(min)
            count += 1
        return None
    
    def promedio(self, records, keys, field):
        cadena = field.replace('"', '')
        count = 0
        large = len(records)

        for value in keys:
            if value == cadena:
                suma = 0
                i = 0
                while large>i:
                    suma += float(records[i][count])
                    i += 1
                total = float(suma)/float(i)
                return str(round(total, 2))
            count += 1
        return None
    
    def sumar(self, records, keys, field):
        cadena = field.replace('"', '')
        count = 0
        large = len(records)

        for value in keys:
            if value == cadena:
                suma = 0
                i = 0
                while large>i:
                    suma += float(records[i][count])
                    i += 1
                return str(round(suma, 2))
            count += 1
        return None