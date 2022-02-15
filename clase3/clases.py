class Person:
    def __init__(self, _firstname:str, _lastname:str, _dni:int, _age:int) -> None:
        #atributos
        self.__firstname = _firstname
        self.__lastname = _lastname
        self.__dni = _dni
        self.__kind = "base"
        self.age = _age
        
    
    #metodos
    def set_cuit(self, cuit):
        ### habia copiado y pegado mal !!!
        aux = str(cuit)[2:10]
        
        if int(aux) == self.__dni:
            self.__cuit = cuit
        else:
            raise Exception("ese no puede ser tu dni")
    def get_cuit(self):
        return self.__cuit
    def get_dni(self)->int:
        return self.__dni
    
    def set_dni(self, new_dni:int, usertype:str)->None:
        if usertype == "ADMIN":
            self.__dni = new_dni
        else:
            raise Exception("No sos ADMIN")
    
    def get_fullname(self)->str:
        return f'{self.__firstname} {self.__lastname}'

    def set_kind(self, new_kind:str)->None:
        self.kind = new_kind
    
    def add_one_year(self)->list:
        aux = self.age
        self.age +=1
        return [self.age, aux]
        
##########     
        
p1 = Person("Gustavo", "Ghioldi", 25724484, 44)
p2 = Person("Juan", "Prez", 34678890, 30)

print(id(p1))
print(id(p2))
print(type(p1))
print(type(p2))

print(p2.get_fullname())
p1.set_kind("vip")
print(p1.kind)
print(p1.age)
print(p1.add_one_year())
print(p1.age)

print(p1.age)
print(p1.get_dni())
print(p1.set_dni(25724484, "ADMIN"))
print(p1.get_dni())
print(p1.get_dni())

print(p1.get_dni())

### Esto jamas!!!!! por que estas creando una variable con el nombre del atributo
# p1.__dni = 111111
# print(p1.__dni)
p1.set_cuit(23257244849)
print(p1.get_cuit())
