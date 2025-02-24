#Christian Aarón Martínez Ibarra, 240247
print("Control de Estacionamiento.")

car = 0
bike = 0
truck = 0

trec = 0 #total recaudado
tcars = 0 #total de vehículos

maxtimec = 0 #tiempo máximo de carros
maxtimeb = 0 #tiempo máximo de motos
maxtimet = 0 #tiempo máximo de camionetas

hrscar = 0 #horas de carros
hrsbike = 0 #horas de motos
hrstruck = 0 #horas de camionetas

while True:
    try:
        tipo = int(input("Tipo de vehículo a ingresar: \n"
                         "1. Auto 2. Moto 3. Camioneta\n"
                         "0. Terminar\n"
                         "Opción: "))
       
        if tipo == 1:
            hrs = int(input("Ingrese las horas de estancia: "))
            if hrs > 0:
                cobro = hrs * 20
                print(f"Cobro de: ${cobro:,.2f}")
                trec += cobro
                tcars += 1
                car += 1
                hrscar += hrs
                if hrs > maxtimec:
                    maxtimec = hrs
            else:
                print("Menos de 1 hr no tiene cobro")

        elif tipo == 2:
            hrs = int(input("Ingrese las horas de estancia: "))
            if hrs > 0:
                cobro = hrs * 10
                print(f"Cobro de: ${cobro:,.2f}")
                trec += cobro
                tcars += 1
                bike += 1
                hrsbike += hrs
                if hrs > maxtimeb:
                    maxtimeb = hrs
            else:
                print("Menos de 1 hr no tiene cobro.")

        elif tipo == 3:
            hrs = int(input("Ingrese las horas de estancia: "))
            if hrs > 0:
                cobro = hrs * 25
                print(f"Cobro de ${cobro:,.2f}")
                trec += cobro
                tcars += 1
                truck += 1
                hrstruck += hrs
                if hrs > maxtimet:
                    maxtimet = hrs
            else:
                print("Menos de 1 hr no tiene cobro.")

        elif tipo == 0:
            print("Día finalizado, resumen:\n"
                  f"Total recaudado: ${trec:,.2f}\n"
                  f"Cantidad de vehículos atendidos: {tcars:,}\n")
            #promedios
            pcar = hrscar / car if car > 0 else 0
            pbike = hrsbike / bike if bike > 0 else 0
            ptruck = hrstruck / truck if truck > 0 else 0 #solo si hubo ingresos del tipo de vehículo
            print("Promedio de horas por tipo de vehículo:\n"
                  f"Autos: {pcar:.2f} horas\n"
                  f"Motos: {pbike:.2f} horas\n"
                  f"Camionetas: {ptruck:.2f} horas\n")
            #vehículo que más tiempo estuvo
            maxtime = max(maxtimec, maxtimeb, maxtimet)
            if maxtime == maxtimec: tmax = "auto" #tmax: tipo max
            elif maxtime == maxtimeb: tmax = "moto"
            else: tmax = "camioneta"
            print(f"Vehículo que más tiempo estuvo: {tmax} con {maxtime} horas")
            break
        else:
            print("Opción no válida.")

    except ValueError:
        print("Ingrese un número.")
