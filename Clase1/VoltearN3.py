#Christian Aarón Martínez Ibarra, 240247
#no: número, c: centena, d: decena, u: unidad, i: invertido
no=int(input("Ingrese un número de tres dígitos: "))
c=no//100
d=(no//10)%10
u=no%10
#unidad ocupa lugar de centena, decena se mantiene, centena en lugar de la unidad.
i=u*100+d*10+c
print(f"Resultado invertido: {i}")
