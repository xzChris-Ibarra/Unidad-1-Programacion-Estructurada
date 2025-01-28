#Christian Aarón Martínez Ibarra, 240247
#Convertir cantidad de horas, minutos y segundos en el total de segundos.

hrs=float(input("Ingrese la cantidad de horas: "))
mns=float(input("Ingrese la cantidad de minutos: "))
s=float(input("Ingrese la cantidad de segundos: "))
tt=(hrs*3600)+(mns*60)+s
print(f"El total en segundos es: {tt:,}")
