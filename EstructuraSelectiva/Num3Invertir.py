#Christian Aarón Martínez Ibarra, 240247
print("Invertir un número de 3 dígitos.")
try:
    n=int(input("Ingrese un número entre 1 y 999: "))
    if n < 1 or n > 999:
        print("Incorrecto, solo entre 1 y 999.") #Validación.
        exit()
    #Descomposición.
    c=n//100 #centena
    d=(n//100)%10 #decena
    u=n%10 #unidad
    #Ordenarlo invertido.
    i=(u*100)+(d*10)+c
    print(f"El número invertido es: {i}")
except ValueError:
    print("Ingrese solo números.")
    exit()
