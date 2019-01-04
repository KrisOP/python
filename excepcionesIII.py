import math

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

#llamada a la funcion evalueEdad
#print (evalueEdad(-18))#evitar que la edad no puede ser negativa

##nuevo uso de lanzamiento propio de excepciones

def calcularRaiz(num1):
    if num1<0:
        raise ValueError ("El numero no puede ser negativo")
    else:
        return math.sqrt(num1)
op1=int(input("ingrese el numero"))
try:
    print (calcularRaiz(op1))
except ValueError as ErrordeNumerNegativo:#agregamos un alias a error para identificarlo mejor
    print (ErrordeNumerNegativo)

print ("programa terminado")
