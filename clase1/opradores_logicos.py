# == , !=, >, < , >=, <=

print(1 == 1) # True
print(1 == 2)

print(1 != "HOLA") # True
print(1 != 1)

print(12 > -1) # True
print(12 > 100)

print(12 >= -1) # True
print(12 >= 12) # True
print(12 >= 100)

print ((not (1 != 2))) # devuelve lo contrario de lo que compara

print(((1==1) or (1==2))) # al menos una de las 2 condiciones debe ser verdadera para que devuelva True

print(((1==1) and (1==2))) # todas condiciones debe ser verdadera para que devuelva True

print(((1==1) and (2==2))) # todas condiciones debe ser verdadera para que devuelva TrueTrue

l = ["gus", "hola", "chau"]

print("gus" in l) # True
print("hello" in l) #False

d = {"nombre": "Gustavo"}
# in en un diccionario pregunta si esta la llave (key)
print("Gustavo" in d) 
print("nombre" in d)