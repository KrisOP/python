import sqlite3

miConexion=sqlite3.connect("PrimerBase")

miCursor=miConexion.cursor()#crear puntero

#miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50),PRECIO INTEGER, SECCION VARCHAR(20))")


miCursor.execute("INSERT INTO PRODUCTOS VALUES ('BALON',15,'Deportes')")

miConexion.commit()#confirmar cambios hechos a la base de datos
miConexion.close()#cerrar la conexion