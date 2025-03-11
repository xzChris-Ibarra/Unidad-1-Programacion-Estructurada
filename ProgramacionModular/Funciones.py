#Christian Aarón Martínez Ibarra, 240247
import random

def saludar(nombre):
    """
    Esta función recibe un nombre y devuelve un saludo personalizado

    Parámetros:
    nombre (str): El nombre de la persona a saludar

    Retorna:
    str: Un mensaje de saludo personalizado
    """
    mensaje = f"¡Hola, {nombre}! Bienvenido/a al mundo de Programación Modular."
    return mensaje

def contar_vocales(palabra):
    """
    Esta función recibe una palabra y cuenta cuántas vocales tiene.

    Parámetros:
    palabra (str): La palabra de la que se contarán las vocales.

    Retorna:
    int: La cantidad de vocales que contiene la palabra
    """
    vocales = "aeiou"
    cantidad_vocales = 0
    for letra in palabra:
        if letra.lower() in vocales:
            cantidad_vocales += 1
    return cantidad_vocales

def contar_letras(nombre):
    return len(nombre)

def calcular_edad(año_nacimiento):
    año_actual = 2025
    try:
        año_nacimiento = int(año_nacimiento)
        if año_nacimiento > 1940 and año_nacimiento <= 2025:
            return f"Tienes {año_actual - año_nacimiento} años."
        else:
            return "Ingrese un año válido entre 1940 y 2025."
    except ValueError:
        return "Error. Ingrese un número entero válido."

def juego():
    print("Juego Piedra, Papel o Tijeras.")
    print("Se jugará contra la máquina importando la posibilidad 'random'.")

    opciones=["piedra", "papel", "tijeras"]
    usuario=input("Elige piedra, papel o tijeras: ").lower()

    #La máquina elige de forma random.
    computadora=random.choice(opciones)
    print(f"Tú elegiste: {usuario}")
    print(f"La computadora eligió: {computadora}")

    if usuario==computadora:
        return "Empate."
    elif (usuario=="piedra" and computadora=="tijeras") or \
         (usuario=="papel" and computadora== "piedra") or \
         (usuario== "tijeras" and computadora== "papel"):
        return "Ganaste."
    else:
        return "Perdiste."

def convertir_nombre(nombre):
    mayusculas = nombre.upper()
    minusculas = nombre.lower()
    return f"En mayúsculas: {mayusculas}\nEn minúsculas: {minusculas}"

def sumar_numeros():
    try:
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        return f"La suma de {num1} + {num2} es: {num1 + num2}"
    except ValueError:
        return "Ingrese solo números."

