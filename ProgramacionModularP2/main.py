#Christian Aarón Martínez Ibarra, 240247
from utils import *

def main():
    print("\nCalculadora de estadísticas básicas")
    while True:
        try:
            cantidad = int(input("¿Cuántos números deseas ingresar?: "))
            if cantidad > 0:
                break
            else:
                print("Error: Ingresa un número entero positivo.")
        except ValueError:
            print("Ingresa un número válido.")
    #Variables
    suma = suma_cuadrados = 0
    mayor = menor = None
    #Procesar cada número ingresado
    for i in range(1, cantidad + 1):
        num = leer_numero(i)
        suma += num
        suma_cuadrados += num ** 2
        mayor, menor = comparar_numeros(num, mayor, menor)
    #Calcular estadísticas
    media = calcular_media(suma, cantidad)
    varianza = calcular_varianza(suma_cuadrados, suma, cantidad)
    desviacion = calcular_desviacion_estandar(varianza)
    
    print("\nResultados:")
    print(f"Media: {media:.2f}")
    print(f"Varianza: {varianza:.2f}")
    print(f"Desviación estándar: {desviacion:.2f}")
    print(f"Número mayor: {mayor}")
    print(f"Número menor: {menor}")

main()