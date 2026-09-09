'''
Stock

Create:

class Stock:

Create:

add_product(name: str, quantity: int) -> None
remove_product(name: str, quantity: int) -> bool
consulte(name: str) -> int

'''



class Stock:
    def __init__(self):
        self.stock = {}

    def add_product(self,name: str, quantity: int) -> None: 
        self.stock[name] = quantity 

    def remove_product(self,name: str, quantity: int) -> bool:
        if name in self.stock and quantity > 0:
            if self.stock[name] >= quantity:
                self.stock[name] -= quantity
                return True
            return False

    def consult(self, name: str) -> int:
        if name in self.stock:
            return self.stock[name]


stock12 = Stock()
stock12.add_product("TV", 10)
stock12.add_product("Mouse", 5)
stock12.remove_product("Mouse", 1)
print(stock12.consult("Mouse"))