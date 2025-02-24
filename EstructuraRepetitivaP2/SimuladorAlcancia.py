#Christian Aarón Martínez Ibarra, 240247
print("Simulador de Alcancía Digital.")

saldo = 0 #saldo disponible
ops = 0 #operaciones
tdep = 0 #total depositado
tret = 0 #total retirado
maxopd = 0 #operación más grande (depósito)
maxopr = 0 #operación más grande (retiro)

while True:
    try:
        opcion = int(input("Ingrese una opción: \n"
                            "1. Depositar\n"
                            "2. Retirar\n"
                            "3. Salir\n"
                            "Opción: "))
        if opcion == 1:
            monto = float(input("Ingrese monto a depositar: "))
            if monto > 0:
                saldo += monto
                tdep += monto
                ops += 1
                if monto > maxopd:
                    maxopd = monto
            else:
                print("El monto debe ser mayor a 0")

        elif opcion == 2:
            monto = float(input("Ingrese el monto a retirar: "))
            if monto > 0:
                if monto <= saldo:
                    saldo -= monto
                    tret += monto
                    ops += 1
                    if monto > maxopr:
                        maxopr = monto
                else:
                    print("No hay saldo suficiente.")
            else:
                print("El monto debe ser mayor a 0")
        elif opcion == 3:
            print("Finalizando...\n"
                "Resumen: \n"
                f"Saldo disponible: ${saldo:,.2f}\n"
                f"Total de operaciones: {ops}\n"
                f"Monto total depositado: ${tdep:,.2f}\n"
                f"Monto total retirado: ${tret:,.2f}\n"
                f"Operación más grande: ${max(maxopd, maxopr):,.2f}")
            break
        else:
            print("Opción no válida.")
    except ValueError:
        print("Ingrese un número.")
