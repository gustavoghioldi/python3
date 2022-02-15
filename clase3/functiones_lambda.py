def calcular(func,  x1: float, x2: float)->float:
    return func(x1, x2)

sumar = lambda x, y: x+y
potencia = lambda x, y: x**y

resultado_sumar = calcular(sumar, 3, 4)
resultado_potencia = calcular(potencia, 2, 3)

print(resultado_sumar)
print(resultado_potencia)
