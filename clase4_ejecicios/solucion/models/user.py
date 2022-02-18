class User:
    def __init__(self, nombre:str, apellido:str, dni:int)->None:
        self.__nombre = nombre
        self.__apellido = apellido
        self.__dni = int(dni)
        
    def get_nombre(self)->str:
        return self.__nombre
    
    def get_apellido(self)->str:
        return self.__apellido
    
    def get_dni(self)->int:
        return self.__dni
    
        