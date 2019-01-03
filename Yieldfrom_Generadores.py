def devuelve_ciudades(*ciudades):#el asteristicos indica que recibira un numero indeterminado de elementos
    #accediendo a letra por letra del primer elemento de la lista
    for elemento in ciudades:
        #for subElemento in elemento:
        yield from elemento

ciudades_devuelve=devuelve_ciudades("Madrid", "Managua", "Esteli", "Boaco")

print(next(ciudades_devuelve))

print(next(ciudades_devuelve))