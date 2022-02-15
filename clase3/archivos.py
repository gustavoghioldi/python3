#open acepta 3 formas w: write, r: read, a:append

f = open("texto.txt", "w")
f.write("hola archivo\n")
#siempre se cierran todos los archivos
f.close()

f = open("texto.txt", "a")
f.write("chau archivo\n")
f.close()

f = open("texto.txt", "r")
print(f.read())
f.close()

f = open("texto.txt", "r")
print(f.readline())
print("-----------")
print(f.readline())
f.close()

