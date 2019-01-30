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
    ("pelota",20,"jugueteria"),
    ("pantalon",15,"confeccion"),
    ("destornillador",25,"ferreteria")
]

miCursor.executemany("INSERT INTO PRODUCTOS VALUES (null,?,?,?)",productos)

miConexion.commit()#confirmar cambios hechos en base de datos
miConexion.close()