#Inicializar variables.
contador = 0 #Contará cuantos números positivos hay.
acumulador = 0 #Acumulará la suma de los números positivos.
#Pedir 5 números al usuario.
for i in range(1, 6): #En vez de range(5) con 1, 6 directamente se pide el numero y se elimina el i+1
    num = float(input(f"Ingrese el número {i}: "))
    #Si el número es positivo, lo sumamos y contamos.
    if num > 0:
        acumulador += num #Suma el número positivo (+= es acumulador = acumulador + num)
        contador += 1 #Incrementa el contador.
#Calcular el promedio si hubo números positivos.
if contador > 0:
    promedio = acumulador / contador
    print(f"El promedio de los números positivos es: {promedio:,.2f}")
else:
    print("No se ingresaron números positivos.")
