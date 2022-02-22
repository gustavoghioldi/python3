import sqlite3

## conexion si no exoste el archivo lo crea.
conn = sqlite3.connect("database.sqlite")

## creamos un cursor
cursor = conn.cursor()

nombre = "hola"
edad = 34

#cursor.execute("INSERT INTO personas values ( ?, ? )", (nombre, edad))
## asi no se debe hacer
#print(f"INSERT INTO personas values ('{nombre}', {edad})")
#cursor.executescript(f"INSERT INTO personas values ('{nombre}', {edad}); DELETE FROM personas;") 
conn.commit()

conn.close()