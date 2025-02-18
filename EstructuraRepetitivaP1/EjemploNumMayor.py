#Inicializar una variable para almacenar el mayor número.
mayor = 0 #Se usa un valor muy pequeño como referencia incial.
#Pedir 5 números al usuario.
for i in range (5):
    num = float(input(f"Ingrese el número {i+1}: "))
    #Comparar y actualizar el mayor si el número ingresado es mayor.
    if num > mayor:
        mayor = num
#Imprimir el número mayor.
print(f"El número mayor es: {mayor}")
