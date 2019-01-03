"""def generaPares(limite):
    num=1
    miLista=[]
    while num<limite:
        miLista.append(num*2)
        num=num+1

    return miLista

print(generaPares(10))"""

#queremos imprimir los pirmeros 3 elementos
#USO DE GENERADORES
def generaPares(limite):
    num=1
    while num<limite:
        yield num*2#yield construye un objeto iterable
        num=num+1
devuelPares=generaPares(10)

#for i in devuelPares:
 #   print (i)

print (next(devuelPares))#  que devuelve solalamente el primer valor almacenado en el interior del objeto generador

#ENTRE LLAMADA Y LLAMADA EL OBJETO GENERADOR ENTRA EN ESTADO DE SUSPENCION, A LA SIGUIENTE LLAMADA, CONTINUA CON LA LISTA DE NUMEROS
print("Aqui podria ir mas codigo...")

print (next(devuelPares))

print("Aqui podria ir mas codigo...")

print (next(devuelPares))


