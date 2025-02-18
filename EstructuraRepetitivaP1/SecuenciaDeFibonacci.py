#Christian Aarón Martínez Ibarra, 240247
print("Secuencia de Fibonacci, genera los primeros N términos de la secuencia.")
print("La secuencia comienza con 0 y 1, y cada término es la suma de los dos anteriores.")
n = int(input("Introduce un número entero positivo: "))
if n > 0:
    a, b = 0, 1 #Primeros dos términos de la secuencia
    print(a)
    print(b)
    for i in range(2, n): 
        a, b = b, a+b #Asignación múltiple, a toma el valor de b y b toma el valor de a+b
        print(b)
else:
    print("El número debe ser un entero positivo.")
