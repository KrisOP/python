def mensajeEnFuncion():#definiendo funciones

    print ("Hello wordl!")
    print (5+6)

    if 5+1 < 10:
        print ("6 es menor que 10")
    else:
        print ("esta pasado")

mensajeEnFuncion()#llamada a la funcion

mensajeEnFuncion()

mensajeEnFuncion()


#Funciones con PARAMETROS

"""Este es otro comentario"""

def suma(num1,num2):
    print("la suma de num1 y num2 es ")
    return num1+num2

resultado=suma(5,2)
print (resultado)

resultado=suma(4,6)

print (resultado)