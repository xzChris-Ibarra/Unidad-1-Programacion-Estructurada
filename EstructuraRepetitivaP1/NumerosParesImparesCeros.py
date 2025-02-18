#Christian Aarón Martínez Ibarra, 240247
print("Programa que cuenta cuántos números pares, impares y ceros hay en una lista de 10 números.")
pares=0
impares=0
ceros=0
for i in range(10):
    num=int(input("Ingresa un número entero: "))
    if num==0:
        ceros+=1
    elif num%2==0:
        pares+=1
    else:
        impares+=1
print(f"En la lista hay {pares} números pares, {impares} números impares y {ceros} ceros.")
