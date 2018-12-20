#definicion de listas
miLista=["Maria", "Pepe", "Marta","kris"]

miLista2=["ortega","pena"]

#print (miLista[-2])#al escribir el indice en negativo leera del final al inicio

#acceder porcion de lista

#print (miLista[0:3])#acceder a los primeros 3 elementos



"""#agregar elementos a la lista
miLista.append("Sandra")#agregar al final
print (miLista[2:])#desde el 2 hasta el final

miLista.insert(2,"Miriam")#agregar el elemento en la posicion 2

print(miLista[2])

print(miLista[:])#imprimir toda la lista

miLista.extend(["Uriel","Ale","Rona"])#agregar varios elementos a la lista

print(miLista[:])"""

#devolver el indice el elemento
#print(miLista.index("kris"))

#imprimir si un elemento se encuentra en la lista

print("kris" in miLista)#devuelve true

miLista.insert(2,56.6)
print(miLista[:])

miLista.remove("Pepe")#eliminar un elemento

print (miLista[:])

miLista.remove(56.6)

print (miLista[:])

miLista.pop()#elimina el ultimo elemento de la lista

print (miLista[:])

#unir dos listas
miLista3=miLista+miLista2

print(miLista3[:])

#repetir las listas n veces
print("REPETIR LA LISTA3 TRES VECES")
print(miLista3[:]*3)