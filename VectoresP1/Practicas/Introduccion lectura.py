""" 1.
¿Qué es un vector (lista o arreglo)?
Un vector o lista es una estructura de datos que almacena múltiples valores en una sola variable.
En Python, se conocen como listas (list) y pueden contener elementos de diferentes tipos (números,
cadenas, booleanos, etc.).
"""
#Ejemplo:
numeros = [10, 20, 30, 40, 50]
nombres = ["Ana", "Luis", "Pedro"]

""" 2.
Características de una lista en Python.
*Ordenadas: Los elementos tienen una posición específica (índice).
*Modificables (mutables): Se pueden cambiar, agregar o eliminar elementos.
*Permiten duplicados: Puedes tener valores repetidos en una lista.
"""

""" 3.
índices y acceso a elementos.
Cada elemento en la lista tiene una posición (índice), que comienza desde 0.
"""
#Ejemplo:
numeros = [10, 20, 30, 40, 50]
print(numeros[0])  #10
print(numeros[2])  #30
#También se pueden usar índices negativos para acceder desde el final:
print(numeros[-1])  #50 (último elemento)
print(numeros[-2])  #40

""" 4.
Recorrer una lista (Iteración).
Para recorrer una lista se usa un bucle for o while.
"""
#Ejemplo con for:
numeros = [10, 20, 30, 40, 50]
for num in numeros:  #num tomará uno por uno los valores de la lista numeros.
    print(num)       #en la primera iteración, num = 10, en la segunda num = 20, y así sucesivamente hasta recorrer toda la lista.

#Método 2: usando for con range(len(lista))
#otra forma de recorrer una lista es usando su índice con range(len(lista))
numeros = [10, 20, 30, 40, 50]
print("Todos los números con índices:") #len: devuelve la cantidad de elementos en la lista.
for i in range(len(numeros)):           #range: genera los números 0,1,2,3,4,5 (índices de la lista).
    print(f"Índice {i}: {numeros[i]}")  #i: en cada iteración, i será el índice actual de la lista.

#Ejemplo con while:
numeros = [10, 20, 30, 40, 50]
print("Recorriendo con while:")
i = 0  #Inicia el índice en 0
while i < len(numeros):  #El bucle sigue ejecutándose mientras i sea menor que la cantidad de elementos en la lista.
    print(numeros[i])  #Se imprime el valor actual.
    i += 1  #Incrementa el índice para avanzar al siguiente elemento.

#Método 4: Recorrer una lista en orden inverso.
#Para recorrer una lista de atrás hacia adelante, se usa range() con valores decrecientes.
#Ejemplo:
numeros = [10, 20, 30, 40, 50]
print("Recorriendo en orden inverso:")
for i in range(len(numeros)-1, -1, -1):  #Primer -1 es el último índice (50). 2do. -1 indica que la cuenta llegará hasta 0.
    print(numeros[i])                    #-1 en el tercer parámetro significa que vamos en pasos negativos (decrementando).

""" Resumen de cómo recorrer listas:
Método              | Código                                | Características
for directo         | for num in lista:                     | Más simple, sin necesidad de índices.
for con range(len())| for i in range(len(lista)):           | Permite acceder a índices.
while               | while i < len(lista):                 | Requiere un contador manual.
Inverso             | for i in range(len(lista)-1, -1, -1): | Permite recorrer desde el final.
"""

""" 5.
Operaciones básicas con listas.
"""
#Modificar un elemento:
numeros[1] = 25  #Cambia el segundo elemento (20 a 25)
#Agregar elementos:
numeros.append(60)  #Agrega un elemento al final.
numeros.insert(2, 35)  #Inserta 35 en la posición 2
#Eliminar elementos:
numeros.pop(1)  #Elimina el segundo elemento.
numeros.remove(40)  #Elimina el número 40 de la lista.
#Ordenar listas:
numeros.sort()  #Ordena la lista en orden ascendente.
numeros.reverse()  #Invierte el orden de los elementos.

""" 6.
Funciones útiles para listas.
Python tiene funciones que facilitan el manejo de listas:
"""
#Ejemplo:
len(numeros)  #Devuelve la cantidad de elementos.
max(numeros)  #Encuentra el valor máximo.
min(numeros)  #Encuentra el valor mínimo.
sum(numeros)  #Suma todos los valores.

""" 7.
Listas multidimensionales (Matrices)
Una lista puede contener otras listas, formando una matriz (arreglo bidimensional):
"""
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matriz[1][2])  #6 (fila 1, columna 2).

""" Conclusión.
Las listas son estructuras fundamentales en programación, permiten almacenar y manipular
múltiples datos de manera eficiente. Son muy utilizadas en algoritmos, estructuras de datos
y programación modular.
"""
