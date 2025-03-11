#Christian Aarón Martínez Ibarra, 240247

from Funciones import saludar, contar_vocales

#Ejemplo de uso de la función
nombre_usuario = input("Por favor, ingresa tu nombre: ")
saludo = saludar(nombre_usuario)
print(saludo)
#Ejemplo de uso de la función para un segundo usuario
#nombre_usuario2 = input("Por favor, ingresa tu nombre: ")
#saludo2 = saludar(nombre_usuario)
#print(saludo2)

#Ejemplo de uso 2da función
print(f"Tu nombre tiene {contar_vocales(nombre_usuario)} vocales")
