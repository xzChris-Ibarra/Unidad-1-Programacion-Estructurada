#Christian Aarón Martínez Ibarra, 240247
print("Comprobar si un número es múltiplo de otro.")

num1=int(input("Ingrese el primer número: "))
num2=int(input("Ingrese el segundo número: "))
#Comprobar usando el operador módulo, si n1 es divisible por n2 sin dejar residuo.
if num1 % num2 == 0:
    print(f"{num1} es múltiplo de {num2}.")
else:
    print(f"{num1} no es múltiplo de {num2}.")
