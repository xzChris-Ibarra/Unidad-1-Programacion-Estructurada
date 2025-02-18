#Christian Aarón Martínez Ibarra, 240247
print("Tablas de multiplicar del 1 al 3.")
for tabla in range (1, 4): #Se generan las tablas del 1 al 3.
    print(f"\nTabla de multiplicar del {tabla}:") #\n es un salto de línea al mostrarse.
    for num in range (1, 11):
        print(f"{tabla} x {num} = {tabla * num}")
