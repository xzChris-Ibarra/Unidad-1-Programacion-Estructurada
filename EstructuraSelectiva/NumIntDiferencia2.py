#Christian Aarón Martínez Ibarra, 240247
print("Calcular la diferencia entre dos enteros positivos.")
try:
    n1=int(input("Ingrese el primer número: "))
    n2=int(input("Ingrese el segundo número: "))
except ValueError:
    print("Debes ingresar números positivos.")
    exit()
#Calcular diferencia del mayor y el menor.
t=n1-n2
if t<=-1:
    t=t*-1
print(f"La diferencia entre {n1} y {n2} es {t}")
