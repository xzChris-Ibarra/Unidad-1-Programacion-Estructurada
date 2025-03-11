#Christian Aarón Martínez Ibarra, 240247
#Objetivo: Crear un programa modular utilizando funciones en archivos separados que realice diversas operaciones
#con datos proporcionados por el usuario.

#Importamos las funciones desde el otro archivo
from Funciones import *

def mostrar_menu():
    print("\n===== Menú de opciones =====")
    print("1. Saludar.")
    print("2. Contar cuántas letras tiene tu nombre.")
    print("3. Calcular tu edad con tu año de nacimiento.")
    print("4. Jugar a piedra, papel y tijera.")
    print("5. Convertir tu nombre a mayúsculas y minúsculas.")
    print("6. Sumar 2 números.")
    print("0. Salir")
    return input("\nSelecciona una opción con un número del 1 al 6, o 0: ")

def main():
    nombre_usuario = input("Por favor, ingresa tu nombre: ")

    while True:
        opcion = mostrar_menu()
        
        if opcion == "1":
            print(saludar(nombre_usuario))

        elif opcion == "2":
            cantidad_letras = contar_letras(nombre_usuario)
            print(f"Tu nombre '{nombre_usuario}' tiene {cantidad_letras} letras.")
        
        elif opcion == "3":
            año_nacimiento = input("Por favor, ingrese el año en que naciste: ")
            resultado = calcular_edad(año_nacimiento)
            print(resultado)

        elif opcion == "4":
            resultado = juego()
            print(resultado)

        elif opcion == "5":
            print(convertir_nombre(nombre_usuario))
        
        elif opcion == "6":
            print(sumar_numeros())
        
        elif opcion == "0":
            print(f"¡Adiós, {nombre_usuario}!")
            break
        
        input("\nPresione Enter para continuar..")
main()
