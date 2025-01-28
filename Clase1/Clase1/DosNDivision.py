#Christian Aarón Martínez Ibarra, 240247
#Este programa divide y muestra el cociente y residuo.

#x1: número 1, x2: número 2, c: cociente, r: residuo
x1=int(input("Ingrese el primer número entero:"))
x2=int(input("Ingrese segundo número entero: "))
c=x1//x2
r=x1%x2
print(f"{x1} entre {x2} da un cociente de {c} y un resto de {r}.")
