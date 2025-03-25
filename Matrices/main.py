#ejemplo de una matriz 3x3
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
#imprimir la matriz
for i in range(3):#recorrer renglones
    for j in range(3):#recorrer columnas
        print(matriz[i][j], end=" ")#imprimir el valor de la matriz pero saltando renglon
    print()

print("Elementos especificos de la matriz")
#acceder a elementos de la matriz
print(matriz[0][1])  # Accede al elemento en la fila 0, columna 1 (valor: 2)
print(matriz[2][2])  # Accede al elemento en la fila 2, columna 2 (valor: 9)
print("")

# Sumar dos matrices
# Definir dos matrices
A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]

# Crear una matriz vacía del mismo tamaño
resultado = [[0, 0], [0, 0]]

# Sumar las matrices
for i in range(len(A)):  
    for j in range(len(A[0])):  
        resultado[i][j] = A[i][j] + B[i][j]  

# Imprimir resultado
for fila in resultado:
    print(fila)