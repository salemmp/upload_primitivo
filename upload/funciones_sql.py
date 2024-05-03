import sqlite3


def agregar_ruta(ruta_completa):
    con=sqlite3.connect('rutas.db')
    cursor=con.cursor()
    cursor.execute(""" INSERT INTO rutas (ruta) VALUES (?)""",(ruta_completa,))
    con.commit()
    con.close()
    return 'añadido exitosamente'


def mostrar_imagenes():
    con=sqlite3.connect('rutas.db')
    cursor=con.cursor()
    cursor.execute(""" SELECT * FROM rutas""")
    lista= cursor.fetchall()
    con.close()
    return lista