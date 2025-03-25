#Christian Aarón Martínez Ibarra, 240247
#Práctica: Operaciones con Matrices en Python.
""" Parte 1. Definir una Matriz en Python.
1. Crea una matriz de 3x3 con valores enteros definidos manualmente.
2. Imprime la matriz en formado de tabla. 
Ejemplo: 
1 2 3
4 5 6
7 8 9
"""
matriz3x3 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for i in range(3):
    for j in range(3):
        print(matriz3x3[i][j], end=" ")
    print()
""" Parte 2. Suma de Dos Matrices.
1. Define dos matrices de tamaño 2x3 con valores enteros.
2. Suma ambas matrices posición por posición y almacena el resultado en una nueva matriz.
3. Muestra la matriz resultante en consola.
"""
matrizA = [
    [1, 2, 5],
    [3, 4, 6]
]
matrizB = [
    [5, 6, 9],
    [7, 8, 6]
]
resultado_suma = [
    [0, 0, 0],
    [0, 0, 0]
]
for i in range(len(matrizA)):
    for j in range(len(matrizA[0])):
        resultado_suma[i][j] = matrizA[i][j] + matrizB[i][j]
print("Matriz resultante de la suma:")
for fila in resultado_suma:
    print(fila)
""" Parte 3. Transponer una Matriz.
1. Escribir un programa que calcule la matriz transpuesta de una matriz dada.
2. La transpuesta se obtiene intercambiando filas por columnas.
"""
matriz_original = [
    [1, 2, 3],
    [4, 5, 6], 
]
#dimensiones de matriz original
filas = len(matriz_original)
columnas = len(matriz_original[0])
#matriz transpuesta vacía 3x2
transpuesta = []
for i in range(columnas):
    fila = []
    for j in range(filas):
        fila.append(0) #Iniciar en ceros
    transpuesta.append(fila) 
#intercambiar filas por columnas
for i in range(filas):
    for j in range(columnas):
        transpuesta[j][i] = matriz_original[i][j] #indices invertidos
print("Matriz original:")
for fila in matriz_original:
    print(fila)
print("Matriz transpuesta:")
for fila in transpuesta:
    print(fila)
""" Parte 4.
*¿Cómo modificar el código para sumar matrices de cualquier tamaño?
*¿Cómo se podría multiplicar matrices sin usar librerías externas?
"""
from funciones import sumar_matrices
matrizPrueba = [
    [2, 4, 6],
    [1, 3, 5],
    [7, 8, 9]
]
matrizPrueba2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]
if len(matrizPrueba) == len(matrizPrueba2) and len(matrizPrueba[0]) == len(matrizPrueba2[0]):
    resultado_sum = sumar_matrices(matrizPrueba, matrizPrueba2)
    print("Matriz resultante de suma:")
    for fila in resultado_sum:
        print(fila)
else:
    print("Las matrices deben tener el mismo tamaño para sumarlas.")

from funciones import multiplicar_matrices
matriz_Mult = [
    [1, 2, 3],
    [4, 5, 6]
]
matriz_Mult2 = [
    [7, 8],
    [9, 10],
    [11, 12]
]
resultado_mult = multiplicar_matrices(matriz_Mult, matriz_Mult2)
if resultado_mult:
    print("Matriz resultante de multiplicar:")
    for fila in resultado_mult:
        print(fila)
else:
    print("No es posible multiplicar las matrices porque los tamaños son incompatibles.")
