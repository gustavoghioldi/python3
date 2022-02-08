#Dicionarios

d = {"age": 44, "dni": 23232323, "name": "Gustavo Ghioldi"}

print(d['age'])
print(d['dni'])
print(d['name'])

#MALO!
d_no_se_debe_hacer = {1212: "123123", True: "Hola"}
print(d_no_se_debe_hacer[1212])
print(len(d))

# para borrar
del d['age']
print(d)