for letra in "python":
    if letra=="h":
        continue
    print ("Viendo letra: "+letra)

nombre="kristopher ortega"

contador=0

for i in nombre:
    if i==" ":
        continue#si existe un espacio ignorar las siguientes instrucciones continuando con la sigiente itracion

    contador+=1

print(contador)


"""##FUNCION PASS, DEVUELVE NULL

class miClase:
    pass#es una clase nula"""


##FUNCION ELSE

email=input("introduce tu email")

for i in email:
    if i=="@":
        arroba=True
        break
else:
    arroba=False

print (arroba)