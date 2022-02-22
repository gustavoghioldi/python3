# pip install pymysql
import pymysql

conn = pymysql.connect(
    host="localhost",
    port=3306,
    user="mysql",
    db="test"
)
cursor = conn.cursor()

cursor.execute("CREATE TABLE  IF NOT EXISTS personas (nombre VARCHAR(25), edad INT)")

personas = (
    ("juan", 12),
    ("pedro", 33),
    ("alberto", 23)
)
for nombre, edad in personas:
    cursor.execute("INSERT INTO personas values ( %s, %s )", (nombre, edad))
conn.commit()

conn.close()