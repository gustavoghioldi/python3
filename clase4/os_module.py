import os

print(os.listdir())
print(os.listdir("./clase1"))
print(os.getcwd())

try:
    os.mkdir("hola")
except FileExistsError:
    print("el directorio ya existe")

print(os.path.exists("hola"))
os.system("touch file.txt")
#os.remove("hola/file.txt")
os.rmdir("hola")
print(os.name)
os.system("pip install requests")