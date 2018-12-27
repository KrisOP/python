for i in ["Primavera","verano","otonio","invierno"]:
    print ("Hola ", end=" ")#no haga un salto de linea en la siguiente interaccion

email=False
contador=0
miEmail=input("ingrese su correo  ")
for i in miEmail: #recorre caracter a caracter 
    if (i=="@" or i=="."):
        contador=contador+1   

"""if email:#es equivalente a email==true
    print ("Es un correo valido")
else:
    print("EL correo no es valido")"""

if contador==2:
    print ("email es correcto")
else:
    print ("Email incorrecto")