#Christian Aarón Martínez Ibarra, 240247
print("Canción elefantes sobre la tela de una araña...\n")
elefantes = 1 #Contador de elefantes en 1
while elefantes <= 10:
    #Imprimir la letra de la canción con el número de elefantes actual.
    if elefantes == 1:
        print(f"{elefantes} elefante se columpiaba sobre la tela de una araña, \n"
                "como veía que resistía fue a llamar a otro elefante..\n")
    else:
        print(f"{elefantes} elefantes se columpiaban sobre la tela de una araña, \n"
                "como veían que resistía fueron a llamar a otro elefante..\n")
    if elefantes < 10: #Si el número de elefantes es menor a 10, preguntar cuántos elefantes siguen.
        while True:
            try:
                answer = int(input(f"¿Cuántos elefantes más se columpiarán? ({elefantes + 1}): "))
                if answer == elefantes + 1:
                    break #Respuesta correcta, continuar el ciclo.
                else:
                    print("Respuesta incorrecta, intenta de nuevo.")
            except ValueError:
                print("Respuesta incorrecta, intenta de nuevo.")
    elefantes += 1 #Incrementar el contador de elefantes.
print("¡10 elefantes, fin!")
