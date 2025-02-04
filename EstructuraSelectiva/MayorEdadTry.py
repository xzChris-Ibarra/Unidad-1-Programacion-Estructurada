#Christian Aarón Martínez Ibarra, 240247
print("Verificar la mayoría de edad del usuario.")
#e: edad
#Capturar edad y verificar si el dato es correcto.
try:
    e = int (input("Por favor, ingrese su edad: "))
except ValueError:
    print("Debes ingresar un número válido (mayor a 0).")
    exit()
#Verificación con if y else.
if e >= 18:
    print("Eres mayor de edad. Autorizado para votar y conducir.")
else:
    print("Eres menor de edad. No autorizado para votar y conducir.")
