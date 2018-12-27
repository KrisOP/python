for i in ["Primavera","verano","otonio","invierno"]:
    print ("Hola ", end=" ")#no haga un salto de linea en la siguiente interaccion

email=False
miEmail=input("ingrese su correo  ")
for i in miEmail: #recorre caracter a caracter 
    if (i=="@"):
        email=True    

if email:#es equivalente a email==true
    print ("Es un correo valido")
else:
    print("EL correo no es valido")