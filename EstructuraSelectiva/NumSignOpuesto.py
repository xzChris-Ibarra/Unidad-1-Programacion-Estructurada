#Christian Aarón Martínez Ibarra, 240247
print("Determinar si dos números tienen signos opuestos.")

n1=int(input("Ingrese el primer número: "))
n2=int(input("Ingrese el segundo número: "))
if n1 == 0 or n2 == 0:
    print("Ingrese números distintos de cero")
elif n1 > 0 and n2 < 0 or n1 < 0 and n2 > 0:
    print("Signos Opuestos")
else:
    print("No son Opuestos")
       