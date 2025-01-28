#Christian Aarón Martínez Ibarra, 240247
#Este programa convierte kilómetros a metros, centímetros y milímetros.

#K: Kilómetros, M: Metros, C: Centímetros, ML: Milímetros
K=float(input("Ingrese la distancia a convertir: "))
M=K*1000
C=K*100000
ML=K*1000000
print(f"Metros: {M:,.0f} Centímetros: {C:,.0f} Milímetros: {ML:,.0f}")
