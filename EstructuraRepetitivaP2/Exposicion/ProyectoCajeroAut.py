#Christian Aarón Martínez Ibarra, 240247

print("¡Bienvenido al cajero automático!")
#Variables.
saldo = 0
intentos = 3
ops = 0 #Operaciones
tdep = 0 #Total depositado
tret = 0 #Total retirado
retmax = 0 #Retiro máximo
depmax = 0 #Depósito máximo

#Configuración de PIN por parte del usuario.
while True:
    try:
        pinuser = int(input("Configure su PIN de 4 dígitos: "))
        if pinuser <= 1000 and pinuser <= 9999:
            print("PIN guardado.\n")
            break
        else:
            print("El PIN debe ser de 4 dígitos.")
    except ValueError:
        print("Ingrese solo números.")

#Validación del PIN para acceder.
while intentos > 0:
    try:
        pin = int(input("Ingrese su PIN: "))
        if pin == pinuser:
            print("Acceso autorizado.")
            break
        else:
            intentos -= 1
            print(f"PIN incorrecto, quedan {intentos} intentos.")
    except ValueError:
        print("Ingrese un número válido.")

#Si se acaban los intentos:
if intentos == 0:
    print("Intentos agotados, CUENTA BLOQUEADA.")
else: #Si el acceso es exitoso, se continua al menú.
    while True:
        try:
            print("Menú del Cajero Automático:\n"
                  "1. Consultar saldo\n"
                  "2. Depositar dinero\n"
                  "3. Retirar dinero\n"
                  "4. Cambiar PIN\n"
                  "5. Salir\n")
            op = int(input("Ingrese una opción: ")) #op: opción.

            #Consultar saldo
            if op == 1:
                print(f"Saldo actual: ${saldo:,.2f}")

            #Depositar
            elif op == 2:
                dep = float(input("Ingrese el monto a depositar: ")) #dep: depósito
                if dep > 0:
                    saldo += dep
                    tdep += dep
                    ops += 1
                    if dep > depmax:
                        depmax = dep
                    print(f"Depósito realizado. Nuevo saldo disponible: ${saldo:,.2f}")
                else:
                    print("El monto debe ser mayor a 0.")

            #Retirar 
            elif op == 3:
                ret = float(input("Ingrese el monto a retirar: ")) #ret: retiro
                if ret > 0:
                    if ret <= saldo:
                        saldo -= ret
                        tret += ret
                        ops += 1
                        if ret > retmax:
                            retmax = ret
                        print(f"Retiro realizado. Nuevo saldo disponible: ${saldo:,.2f}")
                    else:
                        print("Saldo insuficiente.")
                else:
                    print("El monto debe ser mayor a 0.")

            #Cambiar PIN
            elif op == 4:
                newpin = int(input("Ingrese nuevo PIN de 4 dígitos: "))
                if newpin <= 1000 and newpin <= 9999:
                    pinuser = newpin
                    print("PIN actualizado.")
                else:
                    print("El PIN debe ser de 4 dígitos.")
            
            #Salir y resumen
            elif op == 5:
                print("Resumen de operaciones:\n"
                      f"Operaciones realizadas: {ops}\n"
                      f"Total depositado: ${tdep:,.2f}\n"
                      f"Total retirado: ${tret:,.2f}\n")
                if depmax > retmax:
                    print(f"Mayor transacción: Depósito de ${depmax:,.2f}")
                else:
                    print(f"Mayor transacción: Retiro de ${retmax:,.2f}")
                break
            else:
                print("Opción no válida.")
        except ValueError:
            print("Ingrese un número válido.")
