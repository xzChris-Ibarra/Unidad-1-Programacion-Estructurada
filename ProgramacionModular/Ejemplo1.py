#Christian Aarón Martínez Ibarra, 240247
#Funciones
def saludar(nombre):
    """
    Esta función recibe un nombre y devuelve un saludo personalizado

    Parámetros:
    nombre (str): El nombre de la persona a saludar

    Retorna:
    str: Un mensaje de saludo personalizado
    """
    mensaje = (f"¡Hola, {nombre}! Bienvenido/a al mundo de Programación Modular.")
    return mensaje
#Ejemplo de uso de la función
nombre_usuario = input("Por favor, ingresa tu nombre: ")
saludo = saludar(nombre_usuario)
print(saludo)
