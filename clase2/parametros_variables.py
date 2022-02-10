def sumar(*args):
    print(args)
    total = 0
    for n in args:
        total += n
    return total

print(sumar(1, 2, 3,33, 333, 11,  33))
print(sumar(1))

def options(**kwargs):
    print(kwargs)
    for i in kwargs:
        print(i+" : "+str(kwargs[i]))
        
options(dni=878323, direccion="asdasd", altura=1.90, saludo="HOLA")


print("-------------------")
#args terminan formando una tupla
#kwars terminan formando un dict 
def completa(a:int, b, *args, c=1000, **kwargs):
    print(a)
    print(b)
    print(args)
    print(c)
    print(kwargs)

completa("hola", "chau", 1, 2, 3, c=90, uno=1111, dos=2222)
