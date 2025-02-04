#Christian Aarón Martínez Ibarra, 240247
print("Encontrar el mayor entre tres números.")

n1 = int(input("Ingrese el primer número: "))
n2 = int(input("Ingrese el segundo número: "))
n3 = int(input("Ingrese el tercer número: "))

if n1 > n2:
    if n1 > n3:
        max = n1
    else:
        max = n3
elif n2 > n3:
        max = n2
else:
    max = n3
print(f"Maximo: {max}")
