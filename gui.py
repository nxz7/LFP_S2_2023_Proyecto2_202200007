import tkinter as tk
from tkinter import ttk, filedialog
from AFD import AFD
from funciones import funciones
from sintactico import sintactico

auto = AFD()
def Analizar_clicked():
    global archivo_abierto, resultado
    text_box.insert(tk.END, "ANALIZANDO ARCHIVO")
    mostrar_console("CONTENIDO ANALIZADO")
    #--------------------SINTACTICO>>>E---
    parser = sintactico(resultado[0], resultado[1])
    consola = parser.analizar_sintactico()
    console.configure(state='normal')
    console.delete(1.0, tk.END)  
    console.insert(tk.END, consola[0])  
    console.configure(state='disabled')

#CARGA Y LEX DE UNA >> ERRORES SOLO LEX
def Cargar_clicked():
    global archivo_abierto, contenido, resultado
    archivo_abierto = filedialog.askopenfilename(filetypes=[("BizData Files", "*.bizdata")])
    if archivo_abierto:
        with open(archivo_abierto, 'r') as bizdata_file:
            contenido = bizdata_file.read()
            text_box.delete(1.0, tk.END)  
            text_box.insert(tk.END, contenido)
            resultado = auto.analizador(contenido)
            auto.imprimir_tokens()
            auto.imprimir_errores()


def mostrar_console(text):
    console.configure(state='normal', bg='light blue')  
    console.insert(tk.END, text + '\n')  
    console.configure(state='disabled')  

archivo_abierto = None
contenido=None
resultado= None
def Reportes_opcion(event):
    global archivo_abierto, contenido
    selected_item = combo_box.get()
    if selected_item == "Errores":
        text_box.delete(1.0, tk.END)
        
        auto.generate_errors_reporte()
        text_box.insert(tk.END, "Reporte de Errores creado bajo el nombre de: erorres_reporte.html")

    elif selected_item == "Tokens":
        text_box.delete(1.0, tk.END)
        auto.generate_tokens_reporte() 
        text_box.insert(tk.END, "Reporte de Tokens creado bajo el nombre de: tokens_reporte.html")

    elif selected_item == "Arbol":
        text_box.delete(1.0, tk.END) 
        text_box.insert(tk.END, "arbol")

root = tk.Tk()
root.title("PROYECTO 2  LFP - 202200007 - ANALISIS LEXICO y SINTACTICO")
root.configure(bg="lemon chiffon")
root.geometry("1300x350") # ventanaaaaaaa

buttonAnalizar = tk.Button(root, text="Analizar", command=Analizar_clicked, bg="white", fg="blue")
buttonCargar = tk.Button(root, text="Cargar", command=Cargar_clicked, bg="white", fg="blue")

combo_box = ttk.Combobox(root, values=["Errores", "Tokens", "Arbol"])
combo_box.set("reportes")
combo_box.bind("<<ComboboxSelected>>", Reportes_opcion)

text_box = tk.Text(root, height=20, width=60) 
text_box.grid(row=0, column=2, rowspan=3, padx=10, pady=10)

console = tk.Text(root, state='disabled', height=20, width=60, bg='light blue') 
console.grid(row=0, column=3, rowspan=3, padx=10, pady=10)

buttonAnalizar.grid(row=0, column=0, padx=10, pady=10)
buttonCargar.grid(row=1, column=0, padx=10, pady=10)

combo_box.grid(row=1, column=1, padx=10, pady=10)

root.mainloop()
print("prueba medidassssssss")