#Christian Aarón Martínez Ibarra, 240247
print("Determinar si la vocal es abierta o cerrada.")
vocal=input("Ingrese una vocal:")
if vocal in "aeiou":
    if vocal in "aeo":
        print(f"La vocal '{vocal}' es abierta.")
    else:
        print(f"La vocal '{vocal}' es cerrada.")
else:
    print("Solo vocales.")
