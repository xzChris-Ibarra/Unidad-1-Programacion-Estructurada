#Christian Aarón Martínez Ibarra, 240247
print("Pedir números mientras no se ingrese uno negativo.")
print("Al final mostrará la suma de los números ingresados.")
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
