#Christian Aarón Martínez Ibarra, 240247
#no: número, d: decena, u: unidad, i: invertido
no=int(input("Ingrese un numero de dos digitos: "))
d=no//10
u=no%10
i=u*10+d
print(f"Resultado invertido: {i}")