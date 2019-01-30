import sqlite3

miConexion=sqlite3.connect("PrimerBase")

miCursor=miConexion.cursor()#crear puntero

#miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50),PRECIO INTEGER, SECCION VARCHAR(20))")


#miCursor.execute("INSERT INTO PRODUCTOS VALUES ('BALON',15,'Deportes')")

variosProductos=[
    ("Camiseta",10,"Deportes"),
    ("Camion",10,"Jugueteria"),
    ("Jarron",10,"Ceramica")
]

#miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)",variosProductos)##ejecuta muchos

#leer datos
miCursor.execute("select * from PRODUCTOS where NOMBRE_ARTICULO='Camion'")
listadeProductos=miCursor.fetchall()#devuelve una lista al ejecutar la consulta y alamacenarla en la variable
#print(listadeProductos)
for productos in variosProductos:
    print ("Nombre Articulo: ",productos[0], " Precio: ",productos[1], "Seccion", productos[2])
miConexion.commit()

miConexion.commit()#confirmar cambios hechos a la base de datos
miConexion.close()#cerrar la conexion