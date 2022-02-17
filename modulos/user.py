from clase4.user import Client

class User:
    def __init__(self, name:str) -> None:
        self.__name = name
        
    def get_name(self):
        return self.__name