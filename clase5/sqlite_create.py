import sqlite3

## conexion si no exoste el archivo lo crea.
conn = sqlite3.connect("database.sqlite")

## creamos un cursor
cursor = conn.cursor()

personas = (
    ("juan", 12),
    ("pedro", 33),
    ("alberto", 23)
)
for nombre, edad in personas:
    cursor.execute("INSERT INTO personas values ( ?, ? )", (nombre, edad))
conn.commit()
conn.close()