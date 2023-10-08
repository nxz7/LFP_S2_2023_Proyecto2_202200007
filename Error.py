class Error:
    def __init__(self, descripcion, fila, columna):
        self.descripcion = descripcion
        self.fila = fila
        self.columna = columna
        
    def __str__(self):
        return f"Error: {self.descripcion}, Fila: {self.fila}, Columna: {self.columna}"
