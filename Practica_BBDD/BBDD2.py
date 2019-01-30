import sqlite3

miConexion=sqlite3.connect("GestionProductos")

miCursor=miConexion.cursor()

miCursor.execute(''' 
                    CREATE TABLE PRODUCTOS (
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    NOMBRE_ARTICULO VARCHAR (50),
                    PRECIO INTEGER,
                    SECCION VARCHAR(20)) 
''')

productos=[
    ("AR01","pelota",20,"jugueteria"),
    ("AR02","pantalon",15,"confeccion"),
    ("AR03","destornillador",25,"ferreteria")
]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?,?)",productos)

miConexion.commit()#confirmar cambios hechos en base de datos
miConexion.close()