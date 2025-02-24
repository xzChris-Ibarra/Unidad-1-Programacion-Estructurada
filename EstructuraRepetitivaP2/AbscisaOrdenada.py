#Christian Aarón Martínez Ibarra, 240247
print("Calcular todas las ordenadas pares de la función:\n"
      "y = f(x) = x * x * x + 1\n"
      "mostrar la abscisa y ordenada para los valores\n"
      "comprendidos entre 0 y 30.\n")
#Abscisa (x): Valor en el eje X. Ordenada (y): Valor en el eje Y
#Recorrer los valores de x desde 0 hasta 30.
for x in range (31): #31 pq range excluye el ultimo número.
    y = x**3 + 1 #Calcular la ordenada. 
    if y % 2 == 0: #Verificar par.
        print(f"Abscisa: {x} y Ordenada: {y}")
