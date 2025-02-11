#Christian Aarón Martínez Ibarra, 240247
print("Juego Piedra, Papel o Tijeras.")
print("Se jugará contra la máquina importando la posibilidad 'random'.")

import random
opc=["piedra", "papel", "tijeras"]
us=input("Elige piedra, papel o tijeras: ")

#La máquina elige de forma random.
comp=random.choice(opc)
print(f"Tú elegiste: {us}")
print(f"La computadora eligió: {comp}")

if us==comp:
    print("Empate")
elif (us=="piedra" and comp=="tijeras") or (us=="papel" and comp== "piedra") or (us== "tijeras" and comp== "papel"):
    print("Ganaste")
else:
    print("Perdiste")
