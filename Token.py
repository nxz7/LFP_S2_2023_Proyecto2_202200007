class Token:
    def __init__(self, lexema, tipo, fila, columna):
        self.lexema = lexema
        self.tipo = tipo
        self.fila = fila
        self.columna = columna

    def __str__(self):
        return f"Lexema: {self.lexema}, Tipo: {self.tipo}, Fila: {self.fila}, Columna: {self.columna}"