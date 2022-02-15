data = str("Hola como estan!")

print(data.startswith("estan!"))
print(data.startswith("hola"))

print(data.endswith("estan!"))
print(data.endswith("chau"))
#lower pasa todo a minuscula
print(data.lower().startswith("hola"))
#upper pasa toda la cadena a mayusculas
print(data.upper())

data = "         Hola como\n estan!"
print(data.strip())
data = "\tHola como\n estan!\n"
print(data)
print(data.strip())
print(type(data))

data = str("Hola como estan! Hola me voy!")
print(data.replace("Hola", "Chau"))
print(data)

print(data.split())

data = "hola:chau:hola:chau"
print(data.split(":"))

nombre = "Ghioldi,        Gustavo Martin"
firstname = nombre.split(",")[1]
lastname = nombre.split(",")[0]
print(type(nombre.split(",")))
print(f'el primer nombre es {firstname.strip()} y el apellido {lastname.strip()}')

print(data.find("hola"))
print(data.find("oooo"))
print(data.count("hola"))

print(data[data.find("chau"):])
print(data.title())
print(data.capitalize())

print("Hola Mundo".swapcase())
