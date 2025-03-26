
# Crear y escribir en un archivo de texto
with open("archivo.txt", "w") as archivo:
    archivo.write("Hola, este es un archivo de texto.\n")
    archivo.write("Esta es la segunda línea.\n")
    archivo.write("Esta es la tercera línea.\n")
    archivo.write("Esta es la cuarta línea.")


# Abrir un archivo en modo lectura
with open("archivo.txt", "r") as archivo:
    contenido = archivo.read()
    print(contenido)  # Mostrará el contenido del archivo

# Escribir en un archivo (sobrescribe si existe), OJO
with open("archivo.txt", "w") as archivo:
    archivo.write("Este es un nuevo contenido.\n")

# Agregar contenido a un archivo existente
with open("archivo.txt", "a+") as archivo:
    archivo.write("xEsta es una nueva línea agregada.\n")
    archivo.write("Y x esta es una nueva línea agregada.\n")
    archivo.seek(0)  # Mover el cursor al inicio del archivo para leer
    contenido = archivo.read()
    print(contenido)  # Mostrará el contenido del archivo

# Leer línea por línea
with open("archivo.txt", "r") as archivo:
    for linea in archivo:
        print(linea.strip("x"))  # La función .strip("x") solo elimina los caracteres "x" al inicio o al final de la cadena, pero no los que están en medio.
        print(linea.replace("x", "")) # eliminar todas las "x" de la línea, usa .replace("x", "")
