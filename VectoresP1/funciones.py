#Función que recibe una lista y retorna la suma de los elementos.
def sumar_vector(vector):
    suma = 0
    for numero in vector:
        suma += numero
    return suma

def encontrar_mayorymenor(vector):
    mayor = vector[0]
    menor = vector[0]
    for numero in vector:
        if numero > mayor:
            mayor = numero
        if numero < menor:
            menor = numero
    return mayor, menor

def filtrar_mayores(vector, numero):
    resultado = []
    for elemento in vector:
        if elemento > numero:
            resultado.append(elemento)
    return resultado

def combinar_vectores(vector1, vector2):
    return vector1 + vector2

def ordenar_vector(vector):
    n = len(vector)
    for i in range(n):
        min_indice = i
        for j in range(i+1, n):
            if vector[j] < vector[min_indice]:
                min_indice = j
        vector[i], vector[min_indice] = vector[min_indice], vector[i]
    return vector
