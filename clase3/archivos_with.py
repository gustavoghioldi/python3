try:
    with open("texto2.md", "w") as f:
        f.writelines(["hola ", "mundo\n", "chau"])
except FileNotFoundError:
    print("no existe el archivo")