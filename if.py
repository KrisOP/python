print ("programa de evaluacion de notas")
#todo valor capturado del teclado es leido como string
nota_alumno=input("Introduzca la nota del alumno")#detener el programa hasta recibir un valor del teclado

def evaluacion(nota):
    valoracion="aprobado"
    if nota<5:
        valoracion="reprobado"
        print (valoracion)
    else:
        print (valoracion)

evaluacion(int(nota_alumno))
            
