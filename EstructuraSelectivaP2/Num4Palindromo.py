#Christian Aarón Martínez Ibarra, 240247
print("Verificar si un número de cuatro dígitos es palíndromo.")
print("Palíndromo: Se lee igual de izquierda a derecha que de derecha a izquierda.")
try:
    n=int(input("Ingrese un número de cuatro dígitos: "))
    #Verificar que sea de cuatro dígitos
    if 1000 <= n <= 9999:
        #Separar los dígitos
        d1=n//1000
        d2=(n//100)%10
        d3=(n//10)%10
        d4=n%10
        #Verificar si es un palíndromo
        if d1 == d4 and d2 == d3:
            print(f"{n} es un número palíndromo.")
        else:
            print(f"{n} no es un número palíndromo.")
    else:
        print("Solo un número de cuatro dígitos.")
except ValueError:
    print("Ingrese un número entero válido.")
