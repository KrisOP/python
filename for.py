for i in ["Primavera","verano","otonio","invierno"]:
    print ("Hola ", end=" ")#no haga un salto de linea en la siguiente interaccion


for i in "krisortega15@hotmail.es":#recorre caracter a caracter 
    if (i=="@"):
        email=True    

if email==True:
    print ("Es un correo valido")
else:
    print("EL correo no es valido")