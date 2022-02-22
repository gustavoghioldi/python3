import sqlite3

## conexion si no exoste el archivo lo crea.
conn = sqlite3.connect("database.sqlite")

## creamos un cursor
cursor = conn.cursor()
nombre = "juan"
cursor.execute("UPDATE personas SET edad=13 WHERE nombre='?'", nombre)
conn.commit()
conn.close()

