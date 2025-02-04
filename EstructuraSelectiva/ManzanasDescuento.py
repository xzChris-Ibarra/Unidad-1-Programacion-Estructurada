#Christian Aarón Martínez Ibarra, 240247
print("La fruteria ofrece las manzanas con descuento según los kilos.")
print("Kilos: 0-2 = 0%. 2.01-5 = 10%. 5.01-10 = 15%. 10.01 o más = 20%.")

try:
    pxk=float(input("Ingrese el precio por kilo: "))
    k=float(input("Ingrese los kilos: "))
    if k <= 2:
        d=0
    elif k <= 5:
        d=.10
    elif k <= 10:
        d=.15
    else:
        d=.20
    pt=k*pxk #precio total=kilos * precio por kilo.
    md=pt*d #monto descuento=precio total * descuento.
    pf=pt-md #precio final=precio total - monto descuento.

    print(f"El precio final es: ${pf:,.2f}")
except ValueError:
    print("Ingrese una cantidad válida de kilos.")
 