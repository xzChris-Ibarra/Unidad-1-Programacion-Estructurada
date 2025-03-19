#Christian Aarón Martínez Ibarra, 240247
# ===============================================================
# PRÁCTICA DE VECTORES Y MATRICES EN PYTHON
# ===============================================================

"""
INSTRUCCIONES:

1. Lee atentamente cada ejercicio antes de empezar a resolverlo.
2. Escribe tu código en los espacios indicados con "Tu código aquí".
3. Guarda este archivo como "practica_vectores2_tunombre.py".
4. Ejecuta tu código para comprobar que funciona correctamente.
5. Asegúrate de que cada ejercicio produce el resultado esperado.

¡Buena suerte!
"""

# ===============================================================
# PARTE 1: MANIPULACIÓN BÁSICA DE VECTORES
# ===============================================================

print("\n=== PARTE 1: MANIPULACIÓN BÁSICA DE VECTORES ===\n")

# --------------------------
# Ejercicio 1: Crear y modificar un vector
# --------------------------
print("\n--- Ejercicio 1: Crear y modificar un vector ---")

# Tu código aquí
# 1. Crea un vector llamado "ciudades" con 5 nombres de ciudades
# 2. Muestra el vector completo
# 3. Agrega una ciudad más al final del vector usando append()
# 4. Muestra el vector 
ciudades = ["Mexicali", "Guadalajara", "Ensenada", "Chicago", "Cancún"]
print("Vector de ciudades:", ciudades)
ciudades.append("Tokyo")
print("Vector actualizado:", ciudades)

# --------------------------
# Ejercicio 2: Recorrer un vector
# --------------------------
print("\n--- Ejercicio 2: Recorrer un vector ---")

numeros = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print("Vector de números:", numeros)

# Tu código aquí
# 1. Recorre el vector usando un ciclo for y muestra cada número
# 2. Muestra solo los números en posiciones pares (0, 2, 4...)
# 3. Muestra los números en orden inverso
print("\nNúmeros en el vector:")
for numero in numeros:
    print(numero)

print("\nNúmeros enb posiciones pares:")
for i in range(0, len(numeros), 2):
    print(numeros[i])

print("\nNúmeros en orden inverso:")
for i in range(len(numeros)-1, -1, -1):
    print(numeros[i])

# --------------------------
# Ejercicio 3: Operaciones con vectores de temperaturas
# --------------------------
print("\n--- Ejercicio 3: Operaciones con vectores de temperaturas ---")

temperaturas = [22.5, 19.8, 25.1, 28.0, 27.5, 30.2, 18.5]
print("Temperaturas de la semana:", temperaturas)

# Tu código aquí
# 1. Calcula y muestra la temperatura máxima
# 2. Calcula y muestra la temperatura mínima
# 3. Calcula y muestra el promedio de temperaturas
# 4. Cuenta cuántos días tuvieron temperaturas superiores a 25 grados
temp_max = max(temperaturas)
print("Tmeperatura máxima:", temp_max)
temp_min = min(temperaturas)
print("Temperatura mínima:", temp_min)
promedio_temps = sum(temperaturas) / len(temperaturas)
print("Promedio de temperaturas es:", round(promedio_temps, 2))
dias_mayor25 = sum(1 for temp in temperaturas if temp > 25)
print("Días con temperaturas arriba de 25 grados:", dias_mayor25)

# --------------------------
# Ejercicio 4: Eliminar elementos de un vector
# --------------------------
print("\n--- Ejercicio 4: Eliminar elementos de un vector ---")

materias = ["Matemáticas", "Español", "Historia", "Ciencias", "Arte", "Educación Física"]
print("Lista de materias:", materias)

# Tu código aquí
# 1. Elimina la primera materia del vector
# 2. Elimina "Historia" del vector (usando remove)
# 3. Elimina la última materia del vector
# 4. Muestra el vector final
materias.pop(0)
print("Lista de materias con la primera eliminada:", materias)
materias.remove("Historia")
print("Lista de materias con Historia eliminada:", materias)
materias.pop(-1)
print("Lista de materias con la última elimiada:", materias)

# --------------------------
# Ejercicio 5: Filtrar elementos de un vector
# --------------------------
print("\n--- Ejercicio 5: Filtrar elementos de un vector ---")

estaturas = [1.65, 1.80, 1.58, 1.75, 1.90, 1.72, 1.68]
print("Estaturas (en metros):", estaturas)

# Tu código aquí
# 1. Crea un nuevo vector llamado "altos" que contenga solo las estaturas mayores a 1.70m
# 2. Crea un nuevo vector llamado "medios" que contenga solo las estaturas entre 1.65m y 1.75m
# 3. Muestra ambos vectores resultantes
altos = [estatura for estatura in estaturas if estatura > 1.70]
medios = [estatura for estatura in estaturas if 1.65 <= estatura <= 1.75]
print("Estaturas mayores a 1.70m:", altos)
print("Estaturas entre 1.65m y 1.75m:", medios)
