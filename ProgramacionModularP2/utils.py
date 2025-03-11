def leer_numero(indice):
    #Solicita al usuario un número válido y lo retorna como flotante
    while True:
        try:
            num = float(input(f"Introduce el número{indice}: "))
            return num
        except ValueError:
            print("Ingresa un número válido.")

def calcular_media(suma, cantidad):
    #Calcula la media aritmética
    return suma / cantidad if cantidad > 0 else 0

def calcular_varianza(suma_cuadrados, suma, cantidad):
    #Calcula la varianza poblacional
    if cantidad > 0:
        return (suma_cuadrados / cantidad) - (suma / cantidad) ** 2
    return 0

def calcular_desviacion_estandar(varianza):
    #Calcula la desviación estándar
    return varianza ** 0.5

def comparar_numeros(num, mayor, menor):
    #Actualiza el número mayor y menor
    if mayor is None or num > mayor:
        mayor = num
    if menor is None or num < menor:
        menor = num
    return mayor, menor
 