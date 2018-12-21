"""miDiccionario={"Alemania":"Berlin", "Francia":"paris","Nicaragua":"Managua"}#declaracion de diccionarios

print(miDiccionario["Nicaragua"])#imprimir datos del diccionario usando las claves

miDiccionario["Italia"]="Lisboa"#agregar un elemento con al diccionario

print (miDiccionario)

miDiccionario["Italia"]="Roma"#cambiar un nuevo valor a la clave "Italia"

print (miDiccionario)

del miDiccionario["Francia"] #eliminar elemento del diccionario con la clave

print (miDiccionario)"""

"""miDiccionario ={"Alemania":"Berlin", 22:"Kris","ortega":12}
print (miDiccionario)
print (miDiccionario[22])

miTupla=["Espania","Argentina","Costa Rica"]

miDiccionario={miTupla[0]:"Madrid",miTupla[1]:"Buenos Aires",miTupla[2]:"San Jose"}#combinando tuplas con diccionarios

#print (miDiccionario[miTupla[1]])
print (miDiccionario["Argentina"])"""

#miDiccionario={23:"Jordan", "nombre":"Jordan","equipo":"chicago", "anillos":[1991,1992,1993,1996,1998]}#definiendo tupla dentro del diccionario
miDiccionario={23:"Jordan", "nombre":"Jordan","equipo":"chicago", "anillos":{"temporadas":[1991,1992,1993,1996,1998]}}#definiendo diccionario y tuplas dentro del diccionario
#print (miDiccionario)

print (miDiccionario["anillos"])

