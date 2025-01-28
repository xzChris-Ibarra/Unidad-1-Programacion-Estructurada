#Christian Aarón Martínez Ibarra, 240247
#Este programa calcula el cobro a realizar por peso.

#py: payaso, mc: muñeca, pt: peso total
py=int(input("Ingrese el número de payasos: "))
mc=int(input("Ingrese el número de muñecas: "))
#Peso total, Peso payaso: 112g, Peso muñeca: 75g
pt=(py*112)+(mc*75) 
#120 pesos por cada 600g: 120/600=0.2 pesos por gramo
costo=pt*0.2
print(f"El peso total del paquete es de: {pt:,.0f} gramos")
print(f"El costo para el envío es de: ${costo:,.2f} pesos.") 
