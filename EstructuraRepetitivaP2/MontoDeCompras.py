#Christian Aarón Martínez Ibarra, 240247
print("Ingresar los montos de las compras de un cliente, se corta el ingreso \n"
      "de datos cuando el usuario ingrese el monto '0'. Al finalizar, informar \n"
      "el total a pagar, si las ventas superan los $1000, se aplicará un descuento \n"
      "del 10%. \n")
total = 0 #Variable para almacenar el total a pagar. 
while True:
    monto = float(input("Ingrese un monto: "))
    if monto == 0: 
        break
    elif monto < 0:
        print("El monto no puede ser negativo.")
    else:
        total += monto #Acumular monto.
if total > 1000:
    desc = total * 0.10
    total -= desc
    print(f"Descuento del 10%, ${desc}")
print(f"El total a pagar es: ${total:,.2f}")
