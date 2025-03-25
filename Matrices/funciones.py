"""
Funciones para sumar y multiplicar matrices.
"""
def sumar_matrices(matriz1, matriz2):
    filas = len(matriz1)
    columnas = len(matriz1[0])
    resultado = [[0 for _ in range(columnas)] for _ in range(filas)] #Crear matriz vacia con el mismo tamaño en comprension de listas.
    #Sumar elementos posición por posición.
    for i in range(filas):
        for j in range(columnas):
            resultado[i][j] = matriz1[i][j] + matriz2[i][j]
    return resultado

def multiplicar_matrices(matriz1, matriz2):
    filasA = len(matriz1)
    columnasA = len(matriz1[0])
    filasB = len(matriz2)
    columnasB = len(matriz2[0])
    
    if columnasA != filasB:
        return None #Verificar si se pueden multiplicar.
    resultado = [[0 for _ in range(columnasB)] for _ in range(filasA)]
    for i in range(filasA):
        for j in range(columnasB):
            for k in range(columnasA):
                resultado[i][j] += matriz1[i][k] * matriz2[k][j]
    return resultado
