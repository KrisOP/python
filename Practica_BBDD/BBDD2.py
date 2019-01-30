import sqlite3

miConexion=sqlite3.connect("GestionProductos")

miCursor=miConexion.cursor()



miConexion.commit()#confirmar cambios hechos en base de datos
miConexion.close()