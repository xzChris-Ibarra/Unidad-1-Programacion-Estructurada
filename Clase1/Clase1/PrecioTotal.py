#Christian Aarón Martínez Ibarra, 240247
#Calcular el precio total y el IVA.

#pt: precio total, i: IVA, pf: precio final, p1: precio artículo 1
p1=float(input("Ingrese el precio del primer artículo: "))
p2=float(input("Ingrese el precio del segundo artículo: "))
p3=float(input("Ingrese el precio del tercer artículo: "))
pt=p1+p2+p3
i=pt*.16
pf=pt*1.16
print(f"El subtotal es: {pt:,} y el monto del IVA es: {i} dando un precio final de: {pf:,}")
