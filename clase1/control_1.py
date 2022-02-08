age = 18

if age >= 18:  #True
    print("Mayor")
else:
    print("Menor")
    

age2 = 70
if age2 < 18: #False
    print("menor")
elif age2 < 65: #False
    print("mayor")
else:
    print("3ra edad")

l = [1, 2, 3]
if l:
    print("lista llena")
else:
    print("lista vacia")
    
estado = "mayor" if age2 > 18 else "menor"

print(estado)
print("-- fin del programa --")
