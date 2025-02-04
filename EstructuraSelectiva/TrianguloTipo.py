#Christian Aarón Martínez Ibarra, 240247
print("Determinar si un triángulo es equilátero, isósceles o escaleno.")
try:
    l1=float(input("Ingrese el primer lado: "))
    l2=float(input("Ingrese el segundo lado: "))
    l3=float(input("Ingrese el tercer lado: "))
    if l1==l2==l3: #Los tres lados son iguales.
        tipo="Equilátero"
    elif l1==l2 or l1==l3 or l2==l3: #Dos lados son iguales.
        tipo="Isósceles"
    else:
        tipo="Escaleno" #Todos los lados son diferentes.
    print(f"El triángulo es {tipo}.")
except ValueError:
    print("Ingrese valores válidos.")
