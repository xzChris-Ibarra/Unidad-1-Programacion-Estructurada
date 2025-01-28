#Christian Aarón Martínez Ibarra, 240247
#Este programa calcula el índice de masa corporal.

#p: peso, e: estatura, mc: masa corporal
p=float(input("Ingrese su peso en kg: "))
e=float(input("Ingrese su estatura en metros:"))
mc=p/(e)**2
print(f"Su índice de masa corporal es: {mc:.2f}.")
