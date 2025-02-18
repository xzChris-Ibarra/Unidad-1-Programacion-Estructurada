#Christian Aarón Martínez Ibarra, 240247
print("Suma de los primeros N números naturales.")
n = int(input("Introduce un número entero positivo: "))
if n > 0:
    suma = 0 #inicializar suma en 0
    for i in range(1, n+1): #Rango de 1 hasta n
        suma += i #acumular suma
    print(f"La suma de los primeros {n} números naturales es: {suma}")
else:
    print("El número debe ser un entero positivo.")
#avanzar de 2 en 2
#for i in range(3, 15, 3):
    #print(i)
#retroceder de 1 en 1
#for i in range(10, 0, -1):
    #print(i)
