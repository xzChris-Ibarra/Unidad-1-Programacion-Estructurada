#Arreglos
n = int(input("Ingrese el tamaño del arreglo: "))
m = int(input("Ingrese el número de múltiplos: "))
A = []
for i in range(0,n):
    A.append(i*m)
print(A)
