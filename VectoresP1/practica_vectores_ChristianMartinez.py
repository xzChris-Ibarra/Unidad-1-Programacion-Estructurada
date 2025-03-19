#Christian Aarón Martínez Ibarra, 240247
# PRÁCTICA DE VECTORES (ARREGLOS) EN PYTHON PARA PRINCIPIANTES
# ===============================================================

"""
INSTRUCCIONES PARA LOS ALUMNOS:

1. Lee atentamente cada ejercicio antes de empezar a resolverlo.
2. Escribe tu código en los espacios indicados con "Tu código aquí".
3. Guarda este archivo como "practica_vectores_tunombre.py".
4. Ejecuta tu código para comprobar que funciona correctamente.
5. Asegúrate de que cada ejercicio produce el resultado esperado.

¡Buena suerte!
"""

# ===============================================================
# PARTE 1: EJERCICIOS BÁSICOS CON VECTORES
# ===============================================================

print("\n=== PARTE 1: EJERCICIOS BÁSICOS CON VECTORES ===\n")

# Recordatorio: Un vector en Python es simplemente una lista de elementos

# --------------------------
# Ejercicio 1: Crear y mostrar un vector de números del 1 al 10
# --------------------------
print("\n--- Ejercicio 1: Crear y mostrar un vector ---")

# Tu código aquí
# Crea un vector llamado "numeros" que contenga los números del 1 al 10
# Luego muestra el vector completo usando print()
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Arreglo de números: ", numeros)

# --------------------------
# Ejercicio 2: Acceder y modificar elementos de un vector
# --------------------------
print("\n--- Ejercicio 2: Acceder y modificar elementos de un vector ---")

# Usamos este vector para el ejercicio
colores = ["rojo", "verde", "azul", "amarillo", "morado"]
print("Vector original:", colores)

# Tu código aquí
# 1. Muestra el primer color del vector
print("Primer color: ", colores[0])
# 2. Muestra el último color del vector
print("Último color: ", colores[-1])
# 3. Cambia "verde" por "naranja"
colores[1] = "naranja"
# 4. Muestra el vector modificado
print("Índice modificado: ", colores[1])

# --------------------------
# Ejercicio 3: Operaciones con vectores de números
# --------------------------
print("\n--- Ejercicio 3: Operaciones con vectores de números ---")

edades = [15, 18, 21, 14, 17, 20, 16]
print("Vector de edades:", edades)

# Tu código aquí
# 1. Calcula y muestra la suma de todas las edades
suma_edades = 0
edad_mayor = edades[0]
edad_menor = edades[0]
for edad in edades:
    suma_edades += edad
    if edad > edad_mayor:
        edad_mayor = edad
    if edad < edad_menor:
        edad_menor = edad
print("Suma de todas las edades: ", suma_edades)
# 2. Calcula y muestra el promedio de las edades (suma dividida por cantidad)
total_edades = len(edades)
promedio = suma_edades / total_edades
print("Promedio de edades:", round(promedio, 2))
# 3. Muestra la edad más alta
print("Edad más alta:", edad_mayor)
# 4. Muestra la edad más baja
print("Edad más baja:", edad_menor)

# --------------------------
# Ejercicio 4: Buscar un elemento en un vector
# --------------------------
print("\n--- Ejercicio 4: Buscar un elemento en un vector ---")

frutas = ["manzana", "banana", "pera", "naranja", "uva", "fresa"]
print("Vector de frutas:", frutas)

# Tu código aquí
# 1. Define una variable buscar = "pera"
# 2. Recorre el vector de frutas con un ciclo for
# 3. Si encuentras la fruta buscada, muestra "Fruta encontrada en la posición X"
# 4. Si no la encuentras, muestra "Fruta no encontrada"
buscar = "pera"
posicion = -1
for i in range(len(frutas)):
    if frutas[i] == buscar:
        posicion = i
        break
if posicion != -1:
    print(f"Fruta encontrada en la posición {posicion + 1}.")
else:
    print("Fruta no encontrada.")

# --------------------------
# Ejercicio 5: Contar elementos que cumplan una condición
# --------------------------
print("\n--- Ejercicio 5: Contar elementos que cumplan una condición ---")

calificaciones = [85, 90, 75, 95, 70, 60, 80, 65, 88, 92]
print("Vector de calificaciones:", calificaciones)

# Tu código aquí
# 1. Cuenta cuántas calificaciones son mayores o iguales a 80
# 2. Cuenta cuántas calificaciones son menores a 70
# 3. Muestra ambos resultados
mayor_80 = 0
menor_70 = 0
for calificacion in calificaciones:
    if calificacion >= 80:
        mayor_80 += 1
    elif calificacion < 70:
        menor_70 += 1
print(f"Total de calificaciones mayores o iguales a 80 es: {mayor_80}")
print(f"Total de calificaciones menores a 70 es: {menor_70}")

# ===============================================================
# PARTE 2: EJERCICIOS CON FUNCIONES Y VECTORES
# ===============================================================

print("\n=== PARTE 2: EJERCICIOS CON FUNCIONES Y VECTORES ===\n")

# --------------------------
# Ejercicio 6: Función para sumar elementos de un vector
# --------------------------
print("\n--- Ejercicio 6: Función para sumar elementos de un vector ---")

# Tu código aquí
# 1. Define una función llamada "sumar_vector" que reciba un vector como parámetro
# 2. La función debe calcular y retornar la suma de todos los elementos
# 3. Prueba la función con el vector [10, 20, 30, 40, 50]
# 4. Muestra el resultado
from funciones import sumar_vector
vector_prueba = [10, 20, 30, 40, 50]
resultado = sumar_vector(vector_prueba)
print(f"La suma del vector {vector_prueba} es: {resultado}")

# --------------------------
# Ejercicio 7: Función para encontrar el mayor y el menor
# --------------------------
print("\n--- Ejercicio 7: Función para encontrar el mayor y el menor ---")

# Tu código aquí
# 1. Define una función llamada "encontrar_mayor_menor" que reciba un vector como parámetro
# 2. La función debe retornar dos valores: el mayor y el menor elemento del vector
# 3. Prueba la función con el vector [35, 15, 42, 98, 23, 7, 61]
# 4. Muestra los resultados
from funciones import encontrar_mayorymenor
valores_prueba = [35, 15, 42, 98, 23, 7, 61]
mayor, menor = encontrar_mayorymenor(valores_prueba)
print(f"En el vector {valores_prueba}:")
print(f"El número mayor es {mayor} y el número menor es: {menor}")

# --------------------------
# Ejercicio 8: Función para filtrar elementos
# --------------------------
print("\n--- Ejercicio 8: Función para filtrar elementos ---")

# Tu código aquí
# 1. Define una función llamada "filtrar_mayores" que reciba un vector y un número como parámetros
# 2. La función debe retornar un nuevo vector que contenga solo los elementos mayores que el número dado
# 3. Prueba la función con el vector [12, 5, 8, 15, 3, 7, 10] y el número 7
# 4. Muestra el vector resultante
from funciones import filtrar_mayores
prueba_vector = [12, 5, 8, 15, 3, 7, 10]
limite = 7
vector_filtrado = filtrar_mayores(prueba_vector, limite)
print(f"Vector de prueba: {prueba_vector}")
print(f"Elementos mayores que {limite}: {vector_filtrado}")

# --------------------------
# Ejercicio 9: Función para combinar dos vectores
# --------------------------
print("\n--- Ejercicio 9: Función para combinar dos vectores ---")

# Tu código aquí
# 1. Define una función llamada "combinar_vectores" que reciba dos vectores como parámetros
# 2. La función debe retornar un nuevo vector que contenga todos los elementos de ambos vectores
# 3. Prueba la función con los vectores [1, 2, 3] y [4, 5, 6]
# 4. Muestra el vector resultante
from funciones import combinar_vectores
vector1 = [1, 2, 3]
vector2 = [4, 5, 6]
resultado = combinar_vectores(vector1, vector2)
print("Vector combinado:", resultado)

# --------------------------
# Ejercicio 10: Función para ordenar un vector
# --------------------------
print("\n--- Ejercicio 10: Función para ordenar un vector ---")

# Tu código aquí
# 1. Define una función llamada "ordenar_vector" que reciba un vector como parámetro
# 2. La función debe ordenar el vector de menor a mayor sin usar .sort() (usa un algoritmo simple)
# 3. Prueba la función con el vector [64, 25, 12, 22, 11]
# 4. Muestra el vector ordenado
from funciones import ordenar_vector
vector_prueba1 = [64, 25, 12, 22, 11]
vector_ordenado = ordenar_vector(vector_prueba1)
print("Vector ordenado:", vector_ordenado)
