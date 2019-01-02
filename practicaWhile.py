import math
numero=int(input("ingresa un numero a calcular su raiz cuadrada"))

intentos=0

while numero<0:
    print ("No se puede calcular la raiz de un numero negativo")

    if intentos==2:
        print ("has consumido demasiados intentos. El programa se ha finalizado")
        break
    numero=int(input("introdu2ce un numero para calcular la raiz cuadrada"))
    if numero<0:
        intentos=intentos+1
    
if intentos<2:
    solucion=math.sqrt(numero)
    print ("la raiz cuadrada de: "+ str(numero)+ "  es "+ str(solucion))