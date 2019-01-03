def devuelve_ciudades(*ciudades):#el asteristicos indica que recibira un numero indeterminado de elementos
    for elemento in ciudades:
        yield elemento

ciudades_devuelve=devuelve_ciudades("Madrid", "Managua", "Esteli", "Boaco")

print(next(ciudades_devuelve))

print(next(ciudades_devuelve))