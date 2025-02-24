print("Ejemplo de ciclo while con entrada del usuario, pedira y sumara los numeros ingresados")
total = 0
contador = 0
while True: 
    try:
        numero = input("Ingresa un número (o escribe 'fin' para terminar):")
        if numero.lower() == "fin":
            break
        numero = int(numero)
        total += numero
        contador += 1
    except ValueError:
        print("Por favor ingrese un número o la palabra 'fin'")
print(f"El total de la suma de los números es: {total}")
print(f"El total de números ingresados es: {contador}")
