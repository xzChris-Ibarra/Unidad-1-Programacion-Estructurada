#Christian Aarón Martínez Ibarra, 240247
print("Calcular el mayor de cinco números.")
try:
    num1=float(input("Ingrese el primer número: "))
    num2=float(input("Ingrese el segundo número: "))
    num3=float(input("Ingrese el tercer número: "))
    num4=float(input("Ingrese el cuarto número: "))
    num5=float(input("Ingrese el quinto número: "))
    #Se asume que el primer número es el mayor.
    mayor=num1
    #Comparar con cada numero, mayor se actualizara dependiendo.
    if num2 > mayor:
        mayor = num2
    if num3 > mayor:
        mayor = num3
    if num4 > mayor:
        mayor = num4
    if num5 > mayor:
        mayor = num5
    #Después de las comparaciones mayor contiene el numero mas grande.
    print(f"El número mayor es: {mayor}")
except ValueError:
    print("Ingrese solo números válidos.")
