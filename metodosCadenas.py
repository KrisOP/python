nombreUsuario=input("Introduce tu nombre ")

print ("Tu nombre es", nombreUsuario.upper())#convertir la cadena en mayuscula
print ("Tu nombre es", nombreUsuario.lower())#minuscula
print ("Tu nombre es", nombreUsuario.capitalize())#primer letra en mayuscula


edad=input("Introduce la edad ")

#print (edad.isdigit())#vdevuelve true si es un numero

while(edad.isdigit()==False):
    print("por favor introduce un valor numerico")
    edad=input("Introduce la edad de nuevo ")

if (int(edad)<18):
    print ("No puede pasar")
else:
    print ("Puede pasar")

