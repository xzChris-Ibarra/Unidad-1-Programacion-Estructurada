#Christian Aarón Martínez Ibarra, 240247
print("Factorial de un número entero positivo.")
n = int(input("Ingresa un número entero positivo: "))
if n >= 0:
    factorial = 1
    for i in range(1, n+1):
        factorial *= i
    print(f"El factorial de {n} es: {factorial}")
else:
    print("El número debe ser un entero positivo.")
