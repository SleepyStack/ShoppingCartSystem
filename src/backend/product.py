class Product:
    def __init__(self, product_id,name: str, price: float, quantity: int):
        self.name = name
        self.product_id = product_id
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"Product id = {self.product_id}, name={self.name}, price={self.price}, quantity={self.quantity}"

class Grocery(Product):
    def __init__(self, product_id, name: str, price: float, quantity: int, expiration_date: str):
        super().__init__(product_id, name, price, quantity)
        self.expiration_date = expiration_date

    def __str__(self):
        return super().__str__() + f", expiration_date={self.expiration_date}"
    
class Clothing(Product):
    def __init__(self, product_id, name: str, price: float, quantity: int, size: str, color: str):
        super().__init__(product_id, name, price, quantity)
        self.size = size
        self.color = color

    def __str__(self):
        return super().__str__() +  f", size={self.size}, color={self.color}"

class Electronics(Product):
    def __init__(self, product_id, name: str, price: float, quantity: int, warranty_period: str):
        super().__init__(product_id, name, price, quantity)
        self.warranty_period = warranty_period

    def __str__(self):
        return super().__str__() + f", warranty_period={self.warranty_period}"
    
class Furniture(Product):
    def __init__(self, product_id, name: str, price: float, quantity: int, material: str):
        super().__init__(product_id, name, price, quantity)
        self.material = material
    def __str__(self):
        return super().__str__() + f", material={self.material}"
    
class Beauty(Product):
    def __init__(self, product_id, name: str, price: float, quantity: int, brand: str):
        super().__init__(product_id, name, price, quantity)
        self.brand = brand

    def __str__(self):
        return super().__str__() + f", brand={self.brand}"
    
class Sport(Product):
    def __init__(self, product_id, name: str, price: float, quantity: int, type_of_sport: str):
        super().__init__(product_id, name, price, quantity)
        self.type_of_sport = type_of_sport

    def __str__(self):
        return super().__str__() + f", type_of_sport={self.type_of_sport}"