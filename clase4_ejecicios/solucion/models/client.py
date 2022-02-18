from models.user import User

class Client(User):
    def __init__(self, nombre: str, apellido: str, dni: int) -> None:
        self.__buys = []
        super().__init__(nombre, apellido, dni)
        
    def add_buy(self, item:str, qt:float)->None:
        self.__buys.append({
            "item":item,
            "qt": float(qt)
        })
        
    def write_in_file(self):
        with open(f"client_{self.get_dni()}.md", "w") as f:
            f.write("Cliente:\n")
            f.write("========\n")
            f.write(f"- Nombre: {self.get_nombre()}\n")
            f.write(f"- Apellido: {self.get_apellido()}\n")
            f.write(f"- DNI: {self.get_dni()}\n\n")
            f.write("Compras:\n")
            f.write("========\n")
            for i in self.__buys:
                f.write(f"- {i['item']}: {i['qt']}\n")