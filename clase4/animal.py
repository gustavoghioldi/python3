class Animal:
    def hablar(self):
        raise Exception("metodo no implementado")
    
class Gato(Animal):
    def hablar(self):
        print("MIAU!!!")
        
class Perro(Animal):
    def hablar(self):
        print("GUAU!!!")
        
a = Animal()
a.hablar()

p = Perro()
p.hablar()
g = Gato()
g.hablar()