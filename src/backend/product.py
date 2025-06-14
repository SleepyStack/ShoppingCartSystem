class Product:
    def __init__(self, product_id,name: str, price: float, quantity: int):
        self.name = name
        self.product_id = product_id
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"Product id = {self.product_id}, name={self.name}, price={self.price}, quantity={self.quantity}"
    
class Physical_product(Product):
    def __init__(self, product_id,name: str, price: float, quantity: int):
        super().__init__(product_id,name, price, quantity)
    
    def __str__(self):
        return super().__str__()

class Digital_product(Product):
    def __init__(self, product_id,name: str, price: float, quantity: int):
        super().__init__(product_id,name, price, quantity)
    def __str__(self):
        return super().__str__()

#Sub classes implementing class Physical_product

class Grocery(Physical_product):
    def __init__(self, product_id, name: str, price: float, quantity: int, expiration_date: str):
        super().__init__(product_id, name, price, quantity)
        self.expiration_date = expiration_date

    def __str__(self):
        return super().__str__() + f", expiration_date={self.expiration_date}"
    
class Clothing(Physical_product):
    def __init__(self, product_id, name: str, price: float, quantity: int, size: str, color: str):
        super().__init__(product_id, name, price, quantity)
        self.size = size
        self.color = color

    def __str__(self):
        return super().__str__() +  f", size={self.size}, color={self.color}"

class Electronics(Physical_product):
    def __init__(self, product_id, name: str, price: float, quantity: int, warranty_period: str):
        super().__init__(product_id, name, price, quantity)
        self.warranty_period = warranty_period

    def __str__(self):
        return super().__str__() + f", warranty_period={self.warranty_period}"
    
class Furniture(Physical_product):
    def __init__(self, product_id, name: str, price: float, quantity: int, material: str):
        super().__init__(product_id, name, price, quantity)
        self.material = material
    def __str__(self):
        return super().__str__() + f", material={self.material}"
    
class Beauty(Physical_product):
    def __init__(self, product_id, name: str, price: float, quantity: int, brand: str):
        super().__init__(product_id, name, price, quantity)
        self.brand = brand

    def __str__(self):
        return super().__str__() + f", brand={self.brand}"
    
class Sport(Physical_product):
    def __init__(self, product_id, name: str, price: float, quantity: int, type_of_sport: str):
        super().__init__(product_id, name, price, quantity)
        self.type_of_sport = type_of_sport

    def __str__(self):
        return super().__str__() + f", type_of_sport={self.type_of_sport}"
    
class Stationary(Physical_product):
    def __init__(self, product_id, name: str, price: float, quantity: int,):
        super().__init__(product_id, name, price, quantity)
    
    def __str__(self):
        return super().__str__()

class Hardware(Physical_product):
    def __init__(self,product_id, name: str, price: float, quantity: int, type_of_hardware: str):
        super().__init__(product_id, name, price, quantity)
        self.type_of_hardware = type_of_hardware

    def __str__(self):
        return super().__str__() + f", type_of_hardware={self.type_of_hardware}"
    
#Sub classes implementing class Digital_product

class Software(Digital_product):
    def __init__(self, product_id, name: str, price: float, quantity: int, license_key: str):
        super().__init__(product_id, name, price, quantity)
        self.license_key = license_key
    def __str__(self):
        return super().__str__() + f", license_key = {self.license_key}"

class Ebook(Digital_product):
    def __init__(self, product_id, name: str, price: float, quantity: int, author: str):
        super().__init__(product_id,name,price,quantity)
        self.author = author
    def __str__(self):
        return super().__str__() + f", author = {self.author}"
    
class Service(Digital_product):
    def __init__(self, product_id, name: str, price: float, quantity: int, duration: str):
        super().__init__(product_id, name, price, quantity)
        self.duration = duration
    def __str__(self):
        return super().__str__() + f", duration = {self.duration}"
    
class MusicProduct(Digital_product):
    def __init__(self, product_id, name: str, price: float, quantity: int, artist: str, album: str, duration: str, audio_format: str):
        super().__init__(product_id, name, price, quantity)
        self.artist = artist
        self.album = album
        self.duration = duration
        self.audio_format = audio_format

    def __str__(self):
        return super().__str__() + f", artist={self.artist}, album={self.album}, duration={self.duration}, audio_format={self.audio_format}"