#Christian Aaron Martinez Ibarra, 240247
print("Tabla de multiplicar dado un número entero, hasta 10.")

mult=0 #Definir la variable antes del for

n=int(input("Cúal tabla de multiplicar deseas saber: ")) #Definir la operación
print(f"La tabla del {n}")
for i in range(10): #Hacer el ciclo con for para un rango de 10 veces
    mult=(i+1)*n ##i: índice (estándar) variable que controla el ciclo en el que vas, 
                 ##empieza en 0, se le suma 1 y se multiplica por n
    print(f"{n}x{i+1}={mult}")
