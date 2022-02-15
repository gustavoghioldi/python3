cadena = "Hola Mundo!"

try:
    print(cadena[0])
    print(cadena[:4])
    print(cadena[4:])
    print(cadena[2:4])
    print(cadena[-1])
    
    
    for i in "HOLA":
        print(i)
    
    print(cadena*3)
    print(cadena+" Chau Mundo!")

    dato = "\tHola\nChau"
    print(dato)
    print(repr(dato)) #nos imprime como lo escribimos
    print(len(dato))

    dato[0] = " " # este es el que rompe type
    print(cadena[100]) # este es el que rompe index
except IndexError:
    print("Problema con el indice")
except TypeError:
    print("Problema con el tipo")
    
    
