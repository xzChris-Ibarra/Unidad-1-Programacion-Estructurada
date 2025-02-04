#Christian Aarón Martínez Ibarra, 240247
print("Este programa indica a qué grupo etario se pertenece.")

try:
    e=int(input("Ingrese su edad: "))
    if e<=6:
        print("Infancia.")
    elif e>6 and e<=12:
        print("Niñez.")
    elif e>12 and e<=20:
        print("Adolescencia.")
    elif e>20 and e<=25:
        print("Juventud.")
    elif e>25 and e<=60:
        print("Adultez.")
    else:
        e>60 or e<=125
        print("Ancianidad.")
except ValueError:
    print("Ingrese solo números enteros.")
    exit()
