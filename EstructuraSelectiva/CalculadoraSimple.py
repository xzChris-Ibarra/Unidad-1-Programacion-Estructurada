#Christian Aarón Martínez Ibarra, 240247
print("Calculadora simple con operaciones básicas.")
try:
    print("Seleccione la operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    opcion = int(input("Ingrese el número de la operación deseada (1-4): "))
    # Verificar si la opción es válida
    if 1<=opcion<=4:
        n1=float(input("Ingrese el primer número: "))
        n2=float(input("Ingrese el segundo número: "))
        if opcion==1:
            r=n1+n2
            op="suma"
        elif opcion==2:
            r=n1-n2
            op="resta"
        elif opcion==3:
            r=n1*n2
            op="multiplicación"
        else: 
            if n2==0:
                print("Error: No se puede dividir entre cero.")
                exit()
            r=n1/n2
            op="división"
        print(f"El resultado de la {op} es: {r:,.2f}")
    else:
        print("Debe ingresar un número entre 1 y 4.")
except ValueError:
    print("Entrada no válida.")
