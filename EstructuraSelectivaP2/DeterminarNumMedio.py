#Christian Aaron Martinez Ibarra, 240247
print("Determinar el número medio de 3 variables.")

num1=int(input("Ingrese el primer número: "))
num2=int(input("Ingrese el segundo número: "))
num3=int(input("Ingrese el tercer número: "))
# Determinar el número medio usando comparaciones
if (num1 > num2 and num1 < num3) or (num1 < num2 and num1 > num3):
    medio = num1
elif (num2 > num1 and num2 < num3) or (num2 < num1 and num2 > num3):
    medio = num2
else:
    medio = num3
print(f"El número medio es: {medio}")
