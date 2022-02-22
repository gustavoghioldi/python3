import sqlite3

## conexion si no exoste el archivo lo crea.
conn = sqlite3.connect("database.sqlite")

## creamos un cursor
cursor = conn.cursor()

cursor.execute("DELETE FROM personas WHERE nombre='juan'")
conn.commit()
conn.close()