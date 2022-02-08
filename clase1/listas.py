
edades = [44,4,  18,44, 44,  47, 80, 75]
#primer digito: desde donde , segundo digito hasta donde, 3er digito salto

print(edades[0:5:2])

c = ["sD", 1, [1, 2, 3, 4], ["sad", None, False],1.23]
#acceder al ultimo elemwento del 2do elemento de la lista principal
print(c[2][-1])

print(type(c))

#append agrega al final de la lista
edades.append(100)
#insert agrega en una posicion especifica
edades.insert(3, 1000)
edades.remove(44)
print(edades)