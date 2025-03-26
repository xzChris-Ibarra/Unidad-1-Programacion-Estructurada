#Christian Aarón Martínez Ibarra, 240247
#Práctica: Manejo de Archivos en Python
""" Instrucciones
*Escribe un programa en Python que resuelva los siguientes puntos.
*Guarda el código en un archivo llamado practica_archivos.py
*Usa la estructura with open() para manejar archivos de forma segura.
"""
""" Parte 1. Crear y Escribir en un archivo
Crea un archivo llamado datos.txt y guarda en el la siguiente información:
*Tu nombre.
*Tu edad.
*Tu lenguaje de programación favorito.
"""
with open("datos.txt", "w") as archivo:
    archivo.write("Nombre: Chris Ibarra\n")
    archivo.write("Edad: 22\n")
    archivo.write("Lenguaje de programación favorito: Python\n")

""" Parte 2. Leer y Mostrar el Contenido del Archivo
*Abre el archivo "datos.txt" en modo lectura y muestra su contenido en pantalla.
"""
with open("datos.txt", "r") as archivo:
    contenido_datos = archivo.read()
    print(contenido_datos)

""" Parte 3. Agregar más información al Archivo
*Añade las siguientes líneas al archivo sin borrar su contenido anterior:
-Ciudad de residencia
-Pasatiempo favorito
"""
print("----- Mostrando archivo actualizado -----")
with open("datos.txt", "a+") as archivo:
    archivo.write("Ciudad de residencia: Mexicali\n")
    archivo.write("Pasatiempo favorito: Videojuegos\n")
    archivo.seek(0)
    contenido_datos = archivo.read()
    print(contenido_datos)

""" Parte 4. Contar las Líneas del Archivo
*Abre el archivo en modo lectura y cuenta cuántas líneas tiene en total.
-Ejemplo de salida esperada:
El archivo tiene 5 líneas.
"""
print("----- Contar total de líneas en archivo -----")
with open("datos.txt", "r") as archivo:
    lineas = archivo.readlines()
    total_lineas = len(lineas)
    print(f"El archivo de datos tiene {total_lineas} líneas en total.\n")

""" Parte 5. Buscar una Palabra en el archivo
*Solicita al usuario una palabra y busca si está presente en el archivo.
-Si la encuentra, muestra: "La palabra 'Python' está en el archivo."
-Si no, muestra: "La palabra 'Java' no está en el archivo."
"""
print("----- Buscar una palabra -----")
buscar_palabra = input("Ingrese la palabra a buscar: ").lower()
with open("datos.txt", "r") as archivo:
    contenido_datos = archivo.read()

if buscar_palabra in contenido_datos.lower():
    print(f"La palabra '{buscar_palabra}' SI está en el archivo.")
else:
    print(f"La palabra '{buscar_palabra}' NO está en el archivo.")
