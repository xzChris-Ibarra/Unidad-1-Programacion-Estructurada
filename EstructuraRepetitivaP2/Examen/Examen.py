#Christian Aarón Martínez Ibarra, 240247
print("Sistema de votación escolar.\n"
      "15 alumnos votarán entre 3 candidatos,\n"
      "1er. lugar será para el Jefe de Grupo,\n"
      "2do. lugar será para el tesorero.\n")

hugo = 0
paco = 0
luis = 0
votos = 0
for i in range(1, 16):
    try:
        print("Bienvenido al menú de votación, candidatos:\n"
          "1. Hugo\n"
          "2. Paco\n"
          "3. Luis\n")
        opcion = int(input("Seleccione una opción: "))
        
        if opcion == 1:
            hugo += 1
            votos += 1
            print("Siguiente votante.")

        elif opcion == 2:
            paco += 1
            votos += 1
            print("Siguiente votante.")

        elif opcion == 3:
            luis += 1
            votos += 1
            print("Siguiente votante.")

        else:
            print("Ingrese una opción válida.")
    except ValueError:
        print("Ingrese una opción válida.")

while votos == 15:
    if hugo > paco and hugo > luis:
        jefegrupo = hugo 
        j = "Hugo"
        if paco > luis:
            tesorero = paco
            t = "Paco"
            g, tercer = "Luis", luis
        else:
            tesorero = luis
            t = "Luis"
            g, tercer = "Paco", paco
    elif paco > hugo and paco > luis:
        jefegrupo = paco
        j = "Paco"
        if hugo > luis:
            tesorero = hugo
            t = "Hugo"
            g, tercer = "Luis", luis
        else:
            tesorero = luis
            t = "Luis"
            g, tercer = "Hugo", hugo
    else:
        jefegrupo = luis
        j = "Luis"
        if hugo > paco:
            tesorero = hugo
            t = "Hugo"
            g, tercer = "Paco", paco
        else:
            tesorero = paco
            t = "Paco"
            g, tercer = "Hugo", hugo
    porc_jefe = (jefegrupo / votos) * 100
    porc_teso = (tesorero / votos) * 100
    porc_terc = (tercer / votos) * 100
    print(f"Ha ganado {j} para Jefe de Grupo con {jefegrupo} votos y %{porc_jefe:.2f},\n"
          f"siguiendole {t} como Tesorero con {tesorero} votos y %{porc_teso:.2f}.\n"
          f"Por último, {g} con %{porc_terc:.2f} muchas gracias por participar!\n")
    break
