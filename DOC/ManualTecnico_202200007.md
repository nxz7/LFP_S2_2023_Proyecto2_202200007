# Lenguajes formales y de Programación
# Segundo semestre 2023
# proyecto 2 
---
# Universidad San Carlos de Guatemala
## _Programador: Natalia Mariel Calderón Echeverría_
## _Carnet: 202200007_
-----
## Descprincion del proyecto
El proyecto consiste en crear un programa que tenga una intefaz grafica amigable con el usuario, en este caso una empresa, que permita analizar lexicamente el contenido de un archivo bizdata para posteriormente realizar una analisis sintactico que permita ejecutar instrucciones de analisis de datos especificas, estos datos analizados son dinamicos.
## Objetivos
* Objetivo General
    * Desarrollar una herramienta capaz de actuar como analizador lexico y analizador sintactico capaz de ejecutar instrucciones especificar que le permita a las empresas cargar y analizar indformacion especifica.
* Objetivos Específicos
    * Desarrollar un analizador lexico a traves del uso de estados.
    * Manejo de caracteres en python.
    * Dessarrollar un analizador sintactico capaz de poder ejecutar instrucciones e indentificar errores

## Requerimientos 
Programado en:
● Python 3.10.2
● Visual Studio Code
● Sistema operativo de 64 bits

---
## Codigo principal

## _Descripcion_
En el archivo gui.py es donde se encuentra todo el codigo relacionado con la intefaz grafica: botones, combobox, textbox, la ventana etc. Es por esas mismas razones que es aqui en donde la clase AFD.py y sintactico.py se unen. Interfaz grafica:

![ObtenerLink](https://i.ibb.co/JcZ62dv/T.png)

Al unicio del programa se despliega una ventana en la que es posible, cargar un archivo de formato bizdata, dicho contenido se despliega en el textbox editable, al momento en el que el archivo se carga  este es analizado lexicamente; Este analisis nos  permite usar el combobox para desplegar los errores y los tokens reconocidos. 
![ObtenerLink](https://i.ibb.co/0nr3f0G/MENU.png)
Boton "cargar":
![ObtenerLink](https://i.ibb.co/zRFgF90/T1.png)

El boton "Analizar" es el que hace un llamado a la clase sintactico.py, que es donde se analizan sintacticamente cada uno de los tokens reconocidos por el analizador lexico al momento de cargar el archivo. Es por eso que se envian como parametros estos mismos, tanto la lista de tokens como la lista de errores. La lista de tokens es analizada con el objetivo de llevar a cabo cada una de estas instrucciones
![ObtenerLink](https://i.ibb.co/XWk7Yk7/T2.png)

La lista de tokens es analizada con el objetivo de llevar a cabo cada una de estas instrucciones, el resultado de dichas operaciones sera mostrado cen la consola celeste, que a diferencia del textbox, esta no es editable. Unicamente muestra los resultados propios de cada uno de las instrucciones, con excepción del reporte > este se genera como archivo html cuyo resultado logicamente no se muestra en la consola. 

  ![ObtenerLink](https://i.ibb.co/3ms91J2/4.png)
  
  # Reportes de tokens y errores
  ![ObtenerLink](https://i.ibb.co/pKdxYNR/es.png)
  ![ObtenerLink](https://i.ibb.co/S6tQMR6/rt.png)
  
## Expresion Regular
  ![ObtenerLink](https://i.ibb.co/w7Ksk8Q/ER-202200007.png)
## AFD
  ![ObtenerLink](https://i.ibb.co/pPKZMDY/AFD-202200007.jpg)
## gramática independiente del contexto 
  ![ObtenerLink](https://i.ibb.co/L5k9gjy/Tipo2-202200007.jpg)