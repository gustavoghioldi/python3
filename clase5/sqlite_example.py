import sqlite3

### CRUD create (insert), read (select), update (update), delete (delete)
### AMB = altas, bajas y modificaciones

## conexion si no exoste el archivo lo crea.
conn = sqlite3.connect("database.sqlite")

## creamos un cursor
cursor = conn.cursor()
## commo creamos una tabla en SQL"
## CREATE TABLE personas (nombre TEXT, edad Numeric)
cursor.execute("CREATE TABLE  IF NOT EXISTS personas (nombre TEXT, edad Numeric)")

conn.close()