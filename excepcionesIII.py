def evalueEdad(edad):

    if edad<0:
        #especificar el tipo de excepcion que lanzara el programa cuando se cumppla la condicion edad<0
        #estas excepciones no se capturan, lo cual no ejecutara las demas instrucciones
        raise TypeError ("no se permiten edades negativas")
    if edad<20:
        print("eres muy joven")
    elif edad<40:
        print("joven")
    elif edad<65:
        print ("eres maduro")
    elif edad<100:
        print("cuidate... estas anciano")

print (evalueEdad(-18))#evitar que la edad no puede ser negativa