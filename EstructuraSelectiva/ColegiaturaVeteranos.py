#Christian Aarón Martínez Ibarra, 240247
print("Calcular colegiatura.")
te=input("Ingrese el tipo de estudiante, Vet o Reg:") #te: tipo de estudiante.
try:
    nm=int(input("Ingrese el número de materias:")) #nm: número de materias.
    if te=="Vet":
        cxm=30 #costo por materia.
        cat="Veterano" #categoria.
    elif te=="Reg":
        cxm=50
        cat="Regular"
    else:
        print("Tipo de estudiante no válido.")
        exit()
    ct=nm*cxm #costo total.
    print(f"Categoría: {cat}")
    print(f"Número de materias: {nm}")
    print(f"Costo total de la colegiatura: ${ct:,.2f}")
except ValueError:
    print("Error: Ingrese un entero válido.")
