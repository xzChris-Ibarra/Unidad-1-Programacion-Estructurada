#Christian Aarón Martínez Ibarra, 240247
#Obtener la cantidad de dinero que recibirá cada área, para cualquier monto de presupuesto.

#x: monto presupuestal, g: ginecología, t: traumatología, p: pediatría
x=int(input("Ingrese el monto total presupuestal: "))
g=x*.40
t=x*.30
p=x*.30
print(f"El presupuesto para Ginecología es: {g:,.2f}. Para Traumatología es: {t:,.2f}. Para Pediatría es: {p:,.2f}.")
