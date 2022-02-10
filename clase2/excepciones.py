num1 = input("ingrese un numero: ")
num2 = input("ingrese un numero: ")

#excepcion creada/lanzadas por nosotros
if int(num1)==3:
    raise ValueError("no me gusta en numero 3")

#excepciones lanzadas por el lenguaje
try:
    print(int(num1)/int(num2))
except ValueError:
    print("uno de los 2 no es un numero entero")
except ZeroDivisionError:
    print("no puedo dividir por cero")
except Exception:
    print("no se lo que paso")
#no se usa nunca
else:
    print("todo salio bien")
#esto se usa cada vez menos
finally:
    print("se termino")

print("HOLA")