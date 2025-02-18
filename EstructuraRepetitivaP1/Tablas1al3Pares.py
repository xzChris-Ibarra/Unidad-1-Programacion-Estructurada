#Christian Aarón Martínez Ibarra, 240247
print("Tabla del 1 al 3 mostrando solo los resultados pares.")
for tabla in range (1, 4):
    print(f"\nTabla de multiplicar del {tabla}:")
    for num in range (1, 11):
        res = tabla*num
        if res %2==0: #verificar si el resultado es par.
            print(f"{tabla} x {num} = {res}")
#El operador módulo % obtiene el residuo de una división, si %2==0 significa que el residuo es 0, o sea, par.
