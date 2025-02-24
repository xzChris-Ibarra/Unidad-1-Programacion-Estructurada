#Christian Aarón Martínez Ibarra, 240247
#Pantalla del celular bloqueada, partiendo de un pin secreto, se intentara desbloquear, 3 intentos.

print("Celular bloqueado, ingrese PIN")

pin = 2112
intentos = 3
while intentos > 0:
    try:
        entrd = int(input("Ingrese PIN: "))
        if entrd == pin:
            print("Login correcto.")
            break
        else:
            intentos -= 1
            if intentos > 0:
                print(f"PIN incorrecto, quedan {intentos} intentos.")
            else:
                print("LLAMANDO A LA POLICIA")
    except ValueError:
        print("Ingrese solo números.")
