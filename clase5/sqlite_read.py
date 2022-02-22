import sqlite3

## conexion si no exoste el archivo lo crea.
conn = sqlite3.connect("database.sqlite")

## creamos un cursor
cursor = conn.cursor()

cursor.execute("SELECT nombre FROM personas")
print(cursor.fetchall())

#debemos hacer otra consulta por q se vacio el cursor
cursor.execute("SELECT edads FROM personas")
print(cursor.fetchone())
print(cursor.fetchone())

try:
    cursor.execute("SELECT edads FROM personas")
except sqlite3.OperationalError:
    print("error en la consulta")
    
conn.close()

