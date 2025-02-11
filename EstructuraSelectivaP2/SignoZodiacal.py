#Christian Aarón Martínez Ibarra, 240247
print("Determinar el signo zodiacal, con base en su día y mes de nacimiento.")
try:
    dia=int(input("Ingrese el día de nacimiento: "))
    mes=int(input("Ingrese el mes de nacimiento (1-12): "))

    if mes < 1 or mes > 12 or dia < 1 or dia > 31:
        print("Fecha no válida.")
        exit()

    if (mes == 3 and dia >= 21) or (mes == 4 and dia <= 19):
        signo = "Aries"

    elif (mes == 4 and dia >= 20) or (mes == 5 and dia <= 20):
        signo = "Tauro"

    elif (mes == 5 and dia >= 21) or (mes == 6 and dia <= 20):
        signo = "Géminis"

    elif (mes == 6 and dia >= 21) or (mes == 7 and dia <= 22):
        signo = "Cáncer"

    elif (mes == 7 and dia >= 23) or (mes == 8 and dia <= 22):
        signo = "Leo"

    elif (mes == 8 and dia >= 23) or (mes == 9 and dia <= 22):
        signo = "Virgo"

    elif (mes == 9 and dia >= 23) or (mes == 10 and dia <= 22):
        signo = "Libra"

    elif (mes == 10 and dia >= 23) or (mes == 11 and dia <= 21):
        signo = "Escorpio"

    elif (mes == 11 and dia >= 22) or (mes == 12 and dia <= 21):
        signo = "Sagitario"

    elif (mes == 12 and dia >= 22) or (mes == 1 and dia <= 19):
        signo = "Capricornio"

    elif (mes == 1 and dia >= 20) or (mes == 2 and dia <= 18):
        signo = "Acuario"

    elif (mes == 2 and dia >= 19) or (mes == 3 and dia <= 20):
        signo = "Piscis"
        
    else:
        print("Fecha no válida.")
        exit()
    print(f"Su signo zodiacal es: {signo}")
except ValueError:
    print("Error: Ingrese valores numéricos válidos.")
