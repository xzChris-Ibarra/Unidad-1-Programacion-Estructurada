#Luis Gerardo Dávalos Velásquez 240278
#Diego Alberto Ruiz De Los Antos 240259
#Christian Aaron Martinez Ibarra 240247
#Karla Erika Marin Lucero 230229

#Sistema de Ejecutivo Bancario

from funciones import *
id_ejecutivo = 123
contraseña = "pass"
intentos = 3
acceso = 0
print("\tSistema Bancario\t\nIngrese sus credenciales de empleado.")
while intentos > 0:
    try:
        id = int(input("Número de Empleado: "))
        if id == id_ejecutivo:
            contra = input("Contraseña: ")
            if contra == contraseña:
                print("Bienvenido empleado *******.")
                acceso = 1
                break
            else:
                intentos -= 1
                print(f"Acesso denegado, {intentos} intentos restantes.")
        else:
            print("Usuario no encontrado.")
    except ValueError:
        print("Ingrese el número de empleado.")

if acceso == 1:
    while True: 
        opc = menu_Ejecutivo()
        if opc == 1:
            indice = validar_cliente()
            if indice != -1:
                while True:
                    opc2 = menu_cliente()
                    if opc2 == 1:
                        imprimir_1_cliente(indice)
                    elif opc2 == 2:
                        deposito(indice)
                    elif opc2 == 3:
                       retiro(indice)
                    elif opc2 == 4:
                        print(evaluar_prestamo(indice))
                        input("Presione enter para continuar...")
                    elif opc2 == 5:
                        abonar_prestamo(indice)
                    elif opc2 == 6:
                        input("\nVolviendo al menú principal. Presione enter para continuar...")
                        break
                    else:
                        input("\nOpción invalida. Presione enter para continuar...")
        elif opc == 2:
            while True:
                opc2 = menu_general()
                if opc2 == 1:
                    imprimir_base_de_datos()
                elif opc2 == 2:
                    while True:
                        opc3 = menu_stats()
                        if opc3 == 1:
                            imprimir_stats(2)
                        elif opc3 == 2:
                            imprimir_stats(4)
                        elif opc3 == 3:
                            imprimir_stats(5)
                        elif opc3 == 4:
                            imprimir_stats(6)
                        elif opc3 == 5:
                            input("\nVolviendo al menú anterior. Presione enter para continuar...")
                            break
                        else:
                            input("\nOpción invalida. Presione enter para continuar...")
                elif opc2 == 3:
                    while True:
                        opc3 = menu_grafica()
                        if opc3 == 1:
                            histograma()
                        elif opc3 == 2:
                            graf_barras()
                        elif opc3 == 3:
                            graf_pastel()
                        elif opc3 == 4:
                            input("\nVolviendo al menú anterior. Presione enter para continuar...")
                            break
                        else:
                            input("\nOpción invalida. Presione enter para continuar...")
                elif opc2 == 4:
                    while True:
                        opc3 = menu_mod_base()
                        if opc3 == 1:
                            dar_de_alta()
                        elif opc3 == 2:
                            dar_de_baja()
                        elif opc3 == 3:
                            input("\nVolviendo al menú anterior. Presione enter para continuar...")
                            break
                        else:
                            input("\nOpción invalida. Presione enter para continuar...")
                elif opc2 == 5:
                    input("\nVolviendo al menú principal. Presione enter para continuar...")
                    break
                else:
                    input("\nOpción invalida. Presione enter para continuar...")
        elif opc == 3:
            print("\nCerrando Sistema. Hasta Luego.")
            break
        else:
            input("\nOpción invalida. Presione enter para continuar...")
else:
    print("Acceso denegado")