#Christian Aarón Martínez Ibarra, 240247
print("\nRegistrar las temperaturas de la última semana de la ciudad, calcular estadísticas como temperatura promedio, máxima y mínima.")
#variables, suma de temperaturas, temperatura máxima y mínima.
sumtemp=0
tempmax=None
tempmin=None
for i in range(7):
    temp = float(input(f"Ingresa la temperatura del día {i+1}: "))
    sumtemp += temp
    if tempmax is None or temp > tempmax:
        tempmax = temp
    if tempmin is None or temp < tempmin:
        tempmin = temp
prom = sumtemp / 7
print(f"La temperatura promedio de la semana fue de {prom:.2f}C, la máxima fue de {tempmax}C y la mínima fue de {tempmin}C.")
