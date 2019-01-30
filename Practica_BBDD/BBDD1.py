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

miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?)",variosProductos)##ejecuta muchos


miConexion.commit()#confirmar cambios hechos a la base de datos
miConexion.close()#cerrar la conexion