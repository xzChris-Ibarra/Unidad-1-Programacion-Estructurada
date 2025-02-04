#Christian Aarón Martínez Ibarra, 240247
print("Juego de Preguntas, solo se responde con: 'Si' o 'No'.")
try:
    p1=input("¿Colón descubrió América? ")
    if p1 != "si":
        print("Respuesta incorrecta.")
        exit()
    p2=input("¿La independencia de México fue en el año 1810? ")
    if p2 != "no":
        print("Respuesta incorrecta.")
        exit()
    p3=input("¿The Doors fue un grupo de rock Americano? ")
    if p3 != "si":
        print("Respuesta incorrecta.")
        exit()
                
    print("¡Has ganado!")

except:
    print("No válido, ingrese solo 'Si' o 'No'.")
