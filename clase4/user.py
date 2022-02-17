class User:
    def __init__(self, username:str, password:str) -> None:
        self.__username = username
        self.__password = password
        self.tags = []
        
    def get_username(self)->str:
        return self.__username
    
    def set_password(self, new_password:str)->None:
        self.__password = new_password
        
    def add_tag(self, new_tag:str)->None:
        self.tags.append(new_tag)
    
    # def test_get_password(self):
    #     return self.__get_password()
    
    def __get_password(self)->str:
        return self.__password

class Client(User):
    def __init__(self, username:str, password:str, address:str )->None:
        self.address = address
        super().__init__(username, password)
        
    def buy(self, product:str,  amount:float):
        print(f"compraste {product} x {amount}")

class VipClient(Client):
    def buy(self, product:str, amount:float):
        print(f"compraste {product} x {amount/(1.05)}")

class Employee(User):
    def __init__(self, username:str, password:str, salary:float )->None:
        self.__salary = salary
        super().__init__(username, password)
        
    def get_salary(self)->float:
        return self.__salary

# c = Client("gus", "pass", "san martin 121212")
# print(c.get_username())
# c.buy("camisa", 1782.90)

# e = Employee("otro", "123456", 100000.90)
# print(e.get_salary())

# vip = VipClient("gus", "121212", "san 232323")
# vip.buy("camisa", 1000)