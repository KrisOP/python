
miTupla=("kris",12,2,1996)#tambien se puede definir tuplas sin necesidad de usar parentesis
miLista=["K","O","P"]

miLista2=list(miTupla)#para convertir una tupla en lista
miTupla2=tuple(miLista)#convertir una lista en tupla

print (miTupla[2])

print (miLista2)
print (miTupla2)

#sirven para manipular las tuplas y listas
print("K" in miLista)
print (miTupla2.count("K"))#cuantos elementos "K" hay
print (len(miTupla))#canitidad de elementos en una tupla
print (len(miLista))#canitidad de elementos en una lista

#tuplas unitarias con unico elemento

tuplaUni=("kris",)

print(len(tuplaUni))


#DESEMPAQUETADO DE TUPLAS

nombre, dia,mes, anio=miTupla#alamcenar en las variables cada elemento de tupla

print(nombre)
print(anio)
print(mes)
print(dia)