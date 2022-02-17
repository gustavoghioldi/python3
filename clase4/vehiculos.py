class Vehiculo:
    def __init__(self, velocidad:int=0)->None:
        self.velocidad = velocidad
        
    def volar(self)->str:
        raise Exception("metodo no implementado")
    def nadar(self)->str:
        raise Exception("metodo no implementado")
    def andar(self)->str:
        raise Exception("metodo no implementado")
    
class Auto(Vehiculo):
    def __init__(self, ruedas:int, velocidad: int = 0 ) -> None:
        self.ruedas = ruedas
        super().__init__(velocidad)
    def andar(self)->None:
        print("se andar por tierra")
        
class Bote(Vehiculo):
    def __init__(self, color:str, velocidad: int = 0 ) -> None:
        super().__init__(velocidad)
        self.color = color
    def nadar(self) -> None:
        print("estoy nandando")

class Anfibio(Bote,Auto):
    def __init__(self, color:str, ruedas:int, velocidad: int = 0 ) -> None:
        Bote.__init__(self, color)
        Auto.__init__(self, ruedas)

# v = Vehiculo()

# a = Auto(100)
# a.andar()
# b = Bote(40)
# b.nadar()

an =Anfibio("rojo", 6)
an.andar()
an.nadar()
print(an.color)
print(an.ruedas)
