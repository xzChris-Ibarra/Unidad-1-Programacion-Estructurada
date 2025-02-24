#Christian Aarón Martínez Ibarra, 240247
print("Se leen 10 números y se muestra cuantos son positivos, negativos y cero.")

pos = 0
neg = 0
cer = 0

for i in range (10):
    num = float(input("Ingrese un número: "))
    if num > 0:
        pos += 1
    elif num < 0:
        neg += 1
    else:
        cer += 1
print(f"Positivos: {pos} Negativos: {neg} Ceros: {cer}")
