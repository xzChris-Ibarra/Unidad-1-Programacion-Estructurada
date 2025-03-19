#Arreglos en Python: Introducción Básica
#1. Crear un arreglo (lista)
print("\n--- Crear Arreglos ---")
numeros = [1, 2, 3, 4, 5]
frutas = ["manzana", "banana", "fresa"]

print("Arreglo de números: ", numeros)
print("Arreglo de frutas: ", frutas)

#2. Acceder a elementos
print("\n--- Acceder a Elementos ---")
print("Primer número:", numeros[0]) #Los indices empiezan en 0
print("Segunda fruta:", frutas[1])  #Segundo elemento en frutas
print("Último número:", numeros[4]) #Último elemento 4 o con -1 

#3. Modificar elementos
print("\n--- Modificar Elementos ---")
print("Arreglo original:", numeros)
numeros[0] = 10 #Cambiar el primer elemento (1 a 10)
print("Después de cambiar:", numeros)

#4. Añadir elementos
#append.(valor): Agrega un elemento al final de la lista.
#insert(posición, valor): Inserta un valor en una posición específica.
print("\n--- Añadir Elementos ---")
frutas.append("naranja") #Añadir al final
print("Después de añadir:", frutas)

numeros.insert(0, 7) #Insertar el número 7 en la primera posición.
print("Después de insertar:", numeros)

#5. Longitud del arreglo
#len(lista): Devuelve la cantidad de elementos en la lista.
print("\n--- Longitud del Arreglo ---")
print("Cantidad de números:", len(numeros))
print("Cantidad de frutas:", len(frutas))

#6. Recorrer un arreglo
#Se usa un bucle for para recorrer la lista e imprimir cada elemento.
print("\n--- Recorrer un Arreglo ---")
print("Todos los números:")
for numero in numeros:
    print(numero)

#7. Recorrer un arreglo inversamente
print("\nTodos los números (inverso):")
for i in range(len(numeros)-1, -1, -1):
    print(numeros[i])

print("\nTodas las frutas:")
for i in range(len(frutas)):
    print(f"Fruta {i+1}: {frutas[i]}")

#8. Ejemplo simple: encontrar el número mayor:
#Se asume que el primer número es el mayor y luego se recorre la lista comparando
#cada número con el actual mayor.
print("\n--- Encontrar el número mayor ---")
numeros_mezclados = [15, 8, 23, 6, 42, 12]
print("Arreglo:", numeros_mezclados)

mayor = numeros_mezclados[0] #Se asume que el primero es el mayor.
for numero in numeros_mezclados:
    if numero > mayor:
        mayor = numero  #Se actualiza si encontramos un número mayor.
print("El número mayor es:", mayor)

""" Resumen Final
*Se crean listas y se pueden acceder a elementos con [].
*Se pueden modificar (numeros[0] = nuevo_valor).
*Se pueden agregar elementos con append() o insert().
*Se puede obtener la longitud con len().
*Se pueden recorrer con for en orden normal o inverso.
*Se puede buscar el mayor número comparando valores en un for.
"""
