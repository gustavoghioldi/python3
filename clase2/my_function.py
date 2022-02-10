## Funciones

def saludo():
    print("HOLA")
    
def suma(num1:int, num2:int)->int:
    if num1>1000 or num2>1000:
        raise ValueError("no puedo sumar numeros mayores a 1000")
    return num1 + num2

def no_hago_nada(a: int, b:float, c:str, d:list):
    pass

print(suma(1000000, 1))

def _sin_address():
    return "Sin direccion"

def person(name:str, dni:int, address=None)->str:
    """
    Esto el la documentacion de la funcion:
    la funciona hace tal o cual cosa
    """
    if address:
        return f"{name} {dni} {address}"
    else:
        return _sin_address()

def my_func(f:any, num1=None, num2=None):
    if num1 and num2:
        return f(num1, num2)
    else:
        f()

print(person("Gus", 1232323))
print(person("Gus", 1232323, "HPo 18082"))
print(person(dni=1212, address="aca", name="Gus"))

my_func(saludo)
print(my_func(suma, 3, 4))

#scope de una variable
num = 10
def aaa(num):
    num +=1
    print(num)

aaa(num)
print(num)