#Christian Aarón Martínez Ibarra, 240247
#Programa que calcula la paga por las horas trabajadas y su coste.

#hr: horas trabajadas, ch: coste por hora, p: paga
hr=float(input("Ingrese las horas trabajadas: "))
ch=float(input("Ingrese el coste por hora: "))
p=ch*hr
print(f"Su paga es de: {p:,.2f}")
