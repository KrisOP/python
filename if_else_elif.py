print ("verificacion de acceso")

edad=int(input("introduce tu edad:  "))

if edad <18:
    print("acceso denegado")
elif edad>100:
    print ("ERROR! No eres un ELFO")
else:
    print("Accediendo...")

