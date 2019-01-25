import sqlite3

miConexion=sqlite3.connect("PrimerBase")

miCursor=miConexion.cursor()#crear puntero

miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50),PRECIO INTEGER, SECCION VARCHAR(20))")

miConexion.close()#cerrar la conexion