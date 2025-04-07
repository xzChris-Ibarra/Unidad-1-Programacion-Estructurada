#Luis Gerardo Dávalos Velásquez 240278
#Diego Alberto Ruiz De Los Antos 240259
#Christian Aaron Martinez Ibarra 240247
#Karla Erika Marin Lucero 230229

import statistics as stat
import matplotlib.pyplot as plt
from random import randint

def menu_Ejecutivo():
    print("\nMenu principal")
    print("1. Atención al cliente.")
    print("2. Movimientos Administrativos.")
    print("3. Cerrar Sistema.")
    try:
        opc = int(input("\nSeleccione una opción: "))
        return opc
    except ValueError:
        input("La opción debe ser un número. Presione enter para continuar...")

def validar_cliente():
    cliente = input("\nIngresa el número de cuenta: ")
    indice = buscar_x_numero_Cuenta(cliente)
    if indice != -1:
        return indice
    input("\nNo se encontro al cliente en la base de datos. Presione enter para continuar...")
    return -1

def buscar_x_numero_Cuenta(num_cuenta):
    indice = 0
    with open("base_de_datos.txt","r") as base_datos:
         for linea in base_datos:
            if linea.split(",")[0] == num_cuenta:
                return indice
            indice += 1
    return -1

def imprimir_1_cliente(indice):
    print("\n")
    with open("base_de_datos.txt","r") as base_datos:
        encabezado = base_datos.readline().strip("\n").split(",")
        cliente = base_datos.readlines()[indice-1].split(",")
        for i in range(9):
            if i != 3:
                print(encabezado[i],": ",cliente[i])
    input("\nPresione enter para continuar...")

def deposito(indice):
    try:
        deposito = float(input("\nIngrese el monto a depositar: "))
        if deposito > 0:
            deposito = round(deposito,2)
            contenido = list()
            with open("base_de_datos.txt","r+") as base_datos:
                contenido = base_datos.readlines()
                cliente = contenido[indice].split(",")
                saldo = float(cliente[4])
                saldo += deposito
                cliente[4] = str(saldo)
                contenido[indice] = ",".join(cliente)
            with open("base_de_datos.txt","w") as base_datos:
                base_datos.writelines(contenido)
                print("\nDeposito realizado con exito.")
            input("\n\nPresione enter para continuar...")
        else:
            input("\nEl deposito debe ser mayor a 0. Presione enter para continuar...")
    except ValueError:
        input("\nSolo se aceptan datos numerico. Presione enter para continuar...")

def retiro(indice):
    try:
        retiro = float(input("\nIngrese el monto a retirar: "))
        if retiro > 0:
            retiro = round(retiro,2)
            contenido = list()
            with open("base_de_datos.txt","r+") as base_datos:
                contenido = base_datos.readlines()
                cliente = contenido[indice].split(",")
                saldo = float(cliente[4])
            if saldo >= retiro:
                saldo -= retiro
                cliente[4] = str(saldo)
                contenido[indice] = ",".join(cliente)
                with open("base_de_datos.txt","w") as base_datos:
                    base_datos.writelines(contenido)
                    print("\nRetiro realizado con exito")
                input("\nPresione enter para continuar...")
            else:
                input("\nNo cuenta con los fondos suficientes. Presione enter para continuar...")
        else:
            input("\nEl monto a retirar debe ser mayor a 0. Presione enter para continuar...")
    except ValueError:
        input("\nSolo se aceptan datos numerico. Presione enter para continuar...")

def evaluar_prestamo(indice):
    contenido = list()
    with open("base_de_datos.txt","r+") as base_datos:
        contenido = base_datos.readlines()
        cliente = contenido[indice].split(",")
    if int(cliente[2]) < 21 or int(cliente[2]) > 75: # 21 < Edad < 75
        return "\nRechazado - Edad fuera de rango"
    if int(cliente[5]) < 1: #Estabilidad laboral < 1
        return "\nRechazado - Poca estabilidad laboral"
    if float(cliente[6]) < 5000: #Ingreso Mensual < 5000
        return "\nRechazado - Ingreso insuficiente"
    if float(cliente[4]) < (float(cliente[6]) * 0.25): #Saldo < Ingreso Mensual/4
        return "\nRechazado - Bajo saldo"
    if int(cliente[7]) < -1: # Historial de prestamos
        return "\nRechazado - Mal historial"
    if float(cliente[8]) > float(cliente[6])*3:
        return "\nPrestamos Rechazado - Adeudos Pendientes"

    monto_maximo = float(cliente[6]) * 2.5 #Ingreso * 2.5
    monto_minimo = float(cliente[6]) * 1.5
    monto_maximo = round(monto_maximo,2)
    monto_minimo = round(monto_minimo,2)
    print(f"\nAprobado \n- Monto máximo: {monto_maximo:.2f} MXN\n- Monto mínimo: {monto_minimo:.2f}")
    while True:
        try:
            prestamo = float(input("Ingrese el monto solicitado (Ingrese 0 para cancelar): "))
            if prestamo > 0 and prestamo <= monto_maximo:
                if prestamo > monto_minimo:
                    break
                else:
                    input("\nEl prestamo debe de ser mayor al monto mínimo")
            elif prestamo > monto_maximo:
                input("\nEl prestamo no puede ser mayor que el monto maximo. Presione enter para continuar...")
            elif prestamo == 0:
                return "Operación Cancelada."
            else:
                input("\nNo se permiten numeros negativos. Presione enter para continuar...")
        except ValueError:
            input("\nSolo se permiten números. Presione enter para continuar...")
    adeudo = float(cliente[8])
    adeudo += prestamo
    histo = int(cliente[7])
    if histo == 0: 
        histo = 1
    elif histo >= 1 and adeudo == monto_maximo:
        histo = -1
    """ elif prestamo == monto_maximo:
        histo -= 1 """
    cliente[8] = str(adeudo)+"\n"
    cliente[7] = str(histo)
    contenido[indice] = ",".join(cliente)
    with open("base_de_datos.txt","w") as base_datos:
        base_datos.writelines(contenido)
    return f"\nPrestamo Aprobado por un monto de : {prestamo:.2f} MXN"

def abonar_prestamo(indice):
    while True:
        try:
            abono = float(input("\nIngresa el monto del abono/inversion (0 para cancelar): "))
            if abono == 0:
                input("\nOperación cancelada. Presione enter para continuar...")
                return
            elif abono < 0:
                input("\nEl abono debe ser un número positivo. Presione enter para continuar...")
            else:
                abono = round(abono,2)
                with open("base_de_datos.txt","r") as base_datos:
                    contenido = base_datos.readlines()
                cliente = contenido[indice].split(",")
                adeudo = round(float(cliente[8]),2) - abono
                historial = int(cliente[7])
                if adeudo < float(cliente[6])*-1.25:
                    historial = 5
                elif adeudo < float(cliente[6])*-1.25:
                    historial = 4
                elif adeudo < float(cliente[6])*-1.25:
                    historial = 3
                elif adeudo < 0:
                    historial == 2
                elif adeudo < float(cliente[6])*3:
                    historial = -1
                cliente[7] = str(historial)
                cliente[8] = str(adeudo)
                contenido[indice] = ",".join(cliente)
                with open("base_de_datos.txt","w") as base_datos:
                    base_datos.writelines(contenido)
                print("\nAbono/Inversión Realizada con exito.")
                return
        except ValueError:
            input("\nSolo se permiten numeros. Presiona enter para continuar...")

def menu_cliente():
    while True:
        print("\nOperación a realizar:")
        print("1. Ver datos.")
        print("2. Deposito.")
        print("3. Retiro.")
        print("4. Prestamos.")
        print("5. Abono/Inversión")
        print("6. Volver.")
        try:
            opc = int(input("Selecciona una opción: "))
            return opc
        except ValueError:
             input("Solo se permiten números. Presione enter para continuar...")

def imprimir_base_de_datos():
    n = 0
    print("\n--------------------------------------\n")
    with open("base_de_datos.txt","r") as base_datos:
                encabezado = base_datos.readline().strip("\n").split(",")
                for linea in base_datos:
                    for i in range(9):
                        if i != 3:
                            print(encabezado[i],": ",linea.split(",")[i])
                    print("\n--------------------------------------\n")
                    n += 1
                    if n == 5:
                        while True:
                            continuar = input("¿Continuar?(y/n): ")
                            if continuar.lower() == "y":
                                n = 0
                                break
                            elif continuar.lower() == "n":
                                input("\nPresione enter para continuar...")
                                return
                            else:
                                print("Opción invalida")
    input("\nPresione enter para continuar...")

def menu_stats():
    while True:
        print("\nSelecciona la categoria de la que quiere ver estadísticas:")
        print("1. Edad.\n2. Saldo\n3. Estabilidad laboral.\n4. Ingreso Mensual.\n5. Volver.")
        try:
            opc = int(input("Selecciona una opción: "))
            return opc
        except ValueError:
            input("\nSolo se permiten números. Presione enter para continuar...")

def obtener_columna_numerica(columna):
    lista = []
    with open("base_de_datos.txt","r+") as base_datos:
        encabezado = base_datos.readline().split(",")[columna]
        for linea in base_datos:
            lista.append(int(linea.split(",")[columna]))
    return encabezado, lista

def imprimir_stats(categoria):
    lista = []
    encabezado, lista = obtener_columna_numerica(categoria)
    print("\nCategoría: ", encabezado)
    print(f"Promedio: {stat.mean(lista):.2f}")
    print(f"Mediana: {stat.median(lista)}")
    print(f"Moda: {stat.mode(lista):.2f}")
    print(f"Desviavión Estandar: {stat.pstdev(lista):.2f}")
    print(f"Varianza: {stat.pvariance(lista):.2f}")
    input("\nPresione enter para continuar...")

def histograma():
    lista = []
    encabezado, lista = obtener_columna_numerica(2)
    plt.figure(figsize=(8,5))
    plt.hist(lista, bins=7, color='skyblue', edgecolor='black')
    plt.xlabel(encabezado)
    plt.ylabel("Número de clientes")
    plt.title("Distribución de edades de los clientes")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

def graf_barras():
    estabilidad = []
    ingreso = []
    encabezado1, estabilidad = obtener_columna_numerica(5)
    encabezado2, ingreso = obtener_columna_numerica(6)
    plt.figure(figsize=(10,5))
    plt.bar(estabilidad, ingreso, color='green', alpha=0.7)
    plt.xlabel(f"{encabezado1} (Años)")
    plt.ylabel(f"{encabezado2} (MXN)")
    plt.title("Relación entre estabilidad laboral e ingreso mensual")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.show()

def graf_pastel():
    estabilidad = []
    x, estabilidad = obtener_columna_numerica(5)
    empleados = 0
    desempleados = 0
    for e in estabilidad:
        if e > 0:
            empleados += 1
        else:
            desempleados += 1
    labels = ["Empleados", "Desempleados"]
    plt.figure(figsize=(6,6))
    plt.pie([empleados, desempleados], labels=labels, autopct='%1.1f%%', colors=['blue', 'orange'], startangle=90)
    plt.title("Proporción de clientes empleados vs. desempleados")
    plt.show()

def menu_grafica():
    while True:
        print("\nGraficas Disponibles Para Analisis.")
        print("1. Histograma de edades")
        print("2. Estabilidad laboral vs. Ingreso mensual")
        print("3. Clientes empleados vs. desempleados")
        print("4. Volver")
        try:
            opc = int(input("Seleccione una opción: "))
            return opc
        except ValueError:
            input("\nSolo se permiten números. Presione enter para continuar...")

def generar_num_cuenta_y_PIN():
    while True:
        banderaNum = 0
        banderaPIN = 0
        num_cuenta = randint(10000,99999)
        PIN = randint(1000,9999)
        str(num_cuenta)
        with open("base_de_datos.txt","r") as base_datos:
            for linea in base_datos:
                if num_cuenta == linea.split(",")[0]:
                    banderaNum = 1
                if PIN == linea.split(",")[3]:
                    banderaPIN = 1
        if banderaNum == 0 and banderaPIN == 0:
            return num_cuenta, PIN

def dar_de_alta():
    print("\nIngrese los Datos del Cliente.")
    while True:
        nombre = input("Ingresa el nombre del nuevo cliente (Ingrese 0 para cancelar): ")
        if nombre != "0":
            while True:
                try:
                    edad = int(input("Ingresa la edad del cliente: "))
                    if edad >= 18:
                        while True:
                            try:
                                estabilidad = int(input("Ingrese la estabilidad laboral (en años) del cliente (0 si esta desempleado): "))
                                if estabilidad > 0:
                                    while True:
                                        try:
                                            ingreso = int(input("Ingrese el ingreso mensual del cliente: "))
                                            break
                                        except ValueError:
                                            input("\nSolo se permiten números en el ingreso mensual. Presione enter para continuar...")
                                elif estabilidad == 0:
                                    ingreso = 0
                                else:
                                    input("\nLa estabilidad laboral debe ser 0 o un número mayor. \nPresione enter para continuar...")
                                cuenta, PIN = generar_num_cuenta_y_PIN()
                                print("\nVista Preliminar.")
                                print("Número de cuenta: ",cuenta)
                                print("Nombre: ",nombre)
                                print("Edad: ",edad)
                                print("PIN: ",PIN)
                                print("Estabilidad Laboral: ",estabilidad)
                                print("Ingreso Mensual: ",ingreso)
                                while True:
                                    confirmar = input("\nConfirmar (y/n): ")
                                    if confirmar.lower() == "y":
                                        nuevo_cliente = str(cuenta)+","+nombre+","+str(edad)+","+str(PIN)+",0,"+str(estabilidad)+","+str(ingreso)+",0,0\n"
                                        with open("base_de_datos.txt","r+") as base_datos:
                                            contenido = base_datos.readlines()
                                        contenido.append(nuevo_cliente)
                                        with open("base_de_datos.txt","w") as base_datos:
                                            base_datos.writelines(contenido)
                                        input("\nCliente Ingresado Correctamente. Presione enter para continuar...")
                                        return
                                    elif confirmar.lower() == "n":
                                        input("\nOperación Cancelada. Presione enter para continuar...")
                                        return
                                    else:
                                        print("Opción invalida")
                            except ValueError:
                                input("Solo se permiten números en la estabilidad laboral. Presione enter para continuar...")
                    else:
                        input("\nEl banco solo permite clientes mayores de edad.\nPresione enter para continuar...")
                        return
                except ValueError:
                    input("Solo se permiten números en la edad.\nPresione enter para continuar...")
        else:
            input("\nOperación Cancelada. Presione enter para continuar...")
            return

def dar_de_baja():
    indice = validar_cliente()
    if indice != -1:
        print("\nDatos del cliente.")
        imprimir_1_cliente(indice)
        with open("base_de_datos.txt","r") as base_datos:
            contenido = base_datos.readlines()
        cliente = contenido[indice].split(",")
        if float(cliente[8]) > 0:
            input("\nBaja incompleta por Adeudo Pendiente. Presione enter para continuar...")
            return
        while True:
            confirmar = input("¿Desea Confirmar la Baja del Cliente? (y/n)")
            if confirmar.lower() == "y":
                try:
                    PIN = int(input("Solicite el PIN al Cliente: "))
                    if PIN == int(cliente[3]):
                        print("\nEntrgue al cliente los siguientes montos.")
                        print("Saldo: ", cliente[4])
                        if float(cliente[8]) < 0:
                            fondo = float(cliente[8]) * -1
                            print("Fondo de inversión: ", fondo)
                        input("Presione enter para dar por finalizado el proceso de baja...")
                        contenido.pop(indice)
                        with open("base_de_datos.txt","w") as base_datos:
                            base_datos.writelines(contenido)
                        input("\nBaja Completa. Presione enter para continar...")
                        return
                    else:
                        input("\nPIN incorrecto. Presione enter para continuar...")
                except ValueError:
                    input("\nSolo se permiten números. Presione enter para continuar...")
            elif confirmar.lower() == "n":
                input("\nOperación Cancelada. Presione enter para continuar...")
                return
            else:
                input("\nOpción invalida. Presione enter para continuar...")
    else:
        return

def menu_mod_base():
    while True:
        print("\nModificar Base de Datos.")
        print("1. Dar de Alta un Nuevo Cliente.")
        print("2. Dar de Baja un Cliente.")
        print("3. Volver.")
        try:
            opc = int(input("Selecciona una opción: "))
            return opc
        except ValueError:
            input("\nSolo se permiten números. Presione enter para continuar...")

def menu_general():
    while True:
        print("\nMovimientos Administrativos.")
        print("1. Ver Base de Datos Completa (De 5 en 5).")
        print("2. Datos Estadísticos.")
        print("3. Gráficos.")
        print("4. Modificar Base de Datos.")
        print("5. Volver.")
        try:
            opc = int(input("Selecciona una opción: "))
            return opc
        except ValueError:
            input("\nSolo se permiten números. Presione enter para continuar...")