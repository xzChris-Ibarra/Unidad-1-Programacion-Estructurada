#Christian Aarón Martínez Ibarra, 240247
#Este programa lee un entero positivo, y suma todos los enteros desde 1 hasta el entero introducido.

#x: entero introducido, s: suma
x=int(input("Ingrese un número entero positivo: "))
s=x*(x+1)//2
print(f"La suma es: {s}")
