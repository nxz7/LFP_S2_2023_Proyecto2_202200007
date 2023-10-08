output = []
error_e = []

def process_line(line, line_num):
    global output, error_e 
    
    line = line.strip()  
    
    if line.startswith('#COMENTARIO'):
        return  
    elif line.startswith('imprimir('):
        if not line.endswith(');'):
            error_e .append(f"Error sintactico: falta ');'  / linea: {line_num}, columna: /")
        string = line.split('"')[1]  
        output.append(string)
    
    elif line.startswith('imprimirln('):
        if not line.endswith(');'):
            error_e .append(f"Error sintactico: falta ');'  / linea: {line_num}, columna: /")
        string = line.split('"')[1] 
        output.append(string + "\n")

with open('prueba_2.bizdata', 'r') as file:
    line_number = 0
    for line in file:
        line_number += 1
        process_line(line, line_number)

# IMPRIMIR
for line in output:
    print(line, end='')

# IMPRIMIR
for error_e  in error_e :
    print(error_e )
