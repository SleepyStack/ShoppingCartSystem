import json

class Product:
    def __init__(self, product_id, name: str, price: float, quantity: int):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"Product id = {self.product_id}, name={self.name}, price={self.price}, quantity={self.quantity}"

    def to_dict(self):
        return {
            "type": "Product",
            "product_id": self.product_id,
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity
        }

    @staticmethod
    def from_dict(data):
        typ = data.get("type", "Product")
        # Mapping type string to the appropriate class
        if typ == "Physical_product":
            return Physical_product.from_dict(data)
        elif typ == "Digital_product":
            return Digital_product.from_dict(data)
        elif typ == "Grocery":
            return Grocery.from_dict(data)
        elif typ == "Clothing":
            return Clothing.from_dict(data)
        elif typ == "Electronics":
            return Electronics.from_dict(data)
        elif typ == "Furniture":
            return Furniture.from_dict(data)
        elif typ == "Beauty":
            return Beauty.from_dict(data)
        elif typ == "Sport":
            return Sport.from_dict(data)
        elif typ == "Stationary":
            return Stationary.from_dict(data)
        elif typ == "Hardware":
            return Hardware.from_dict(data)
        elif typ == "Software":
            return Software.from_dict(data)
        elif typ == "Ebook":
            return Ebook.from_dict(data)
        elif typ == "Service":
            return Service.from_dict(data)
        elif typ == "MusicProduct":
            return MusicProduct.from_dict(data)
        else:
            return Product(data["product_id"], data["name"], data["price"], data["quantity"])

class Physical_product(Product):
    def __init__(self, product_id, name: str, price: float, quantity: int):
        super().__init__(product_id, name, price, quantity)

    def to_dict(self):
        d = super().to_dict()
        d["type"] = "Physical_product"
        return d

    @staticmethod
    def from_dict(data):
        return Physical_product(data["product_id"], data["name"], data["price"], data["quantity"])

class Digital_product(Product):
    def __init__(self, product_id, name: str, price: float, quantity: int):
        super().__init__(product_id, name, price, quantity)

    def to_dict(self):
        d = super().to_dict()
        d["type"] = "Digital_product"
        return d

    @staticmethod
    def from_dict(data):
        return Digital_product(data["product_id"], data["name"], data["price"], data["quantity"])

# Subclasses of Physical_product

class Grocery(Physical_product):
    def __init__(self, product_id, name: str, price: float, quantity: int, expiration_date: str):
        super().__init__(product_id, name, price, quantity)
        self.expiration_date = expiration_date

    def __str__(self):
        return super().__str__() + f", expiration_date={self.expiration_date}"

    def to_dict(self):
        d = super().to_dict()
        d["type"] = "Grocery"
        d["expiration_date"] = self.expiration_date
        return d

    @staticmethod
    def from_dict(data):
        return Grocery(data["product_id"], data["name"], data["price"], data["quantity"], data["expiration_date"])

class Clothing(Physical_product):
    def __init__(self, product_id, name: str, price: float, quantity: int, size: str, color: str):
        super().__init__(product_id, name, price, quantity)
        self.size = size
        self.color = color

    def __str__(self):
        return super().__str__() + f", size={self.size}, color={self.color}"

    def to_dict(self):
        d = super().to_dict()
        d["type"] = "Clothing"
        d["size"] = self.size
        d["color"] = self.color
        return d

    @staticmethod
    def from_dict(data):
        return Clothing(data["product_id"], data["name"], data["price"], data["quantity"], data["size"], data["color"])

class Electronics(Physical_product):
    def __init__(self, product_id, name: str, price: float, quantity: int, warranty_period: str):
        super().__init__(product_id, name, price, quantity)
        self.warranty_period = warranty_period

    def __str__(self):
        return super().__str__() + f", warranty_period={self.warranty_period}"

    def to_dict(self):
        d = super().to_dict()
        d["type"] = "Electronics"
        d["warranty_period"] = self.warranty_period
        return d

    @staticmethod
    def from_dict(data):
        return Electronics(data["product_id"], data["name"], data["price"], data["quantity"], data["warranty_period"])

class Furniture(Physical_product):
    def __init__(self, product_id, name: str, price: float, quantity: int, material: str):
        super().__init__(product_id, name, price, quantity)
        self.material = material

    def __str__(self):
        return super().__str__() + f", material={self.material}"

    def to_dict(self):
        d = super().to_dict()
        d["type"] = "Furniture"
        d["material"] = self.material
        return d

    @staticmethod
    def from_dict(data):
        return Furniture(data["product_id"], data["name"], data["price"], data["quantity"], data["material"])

class Beauty(Physical_product):
    def __init__(self, product_id, name: str, price: float, quantity: int, brand: str):
        super().__init__(product_id, name, price, quantity)
        self.brand = brand

    def __str__(self):
        return super().__str__() + f", brand={self.brand}"

    def to_dict(self):
        d = super().to_dict()
        d["type"] = "Beauty"
        d["brand"] = self.brand
        return d

    @staticmethod
    def from_dict(data):
        return Beauty(data["product_id"], data["name"], data["price"], data["quantity"], data["brand"])

class Sport(Physical_product):
    def __init__(self, product_id, name: str, price: float, quantity: int, type_of_sport: str):
        super().__init__(product_id, name, price, quantity)
        self.type_of_sport = type_of_sport

    def __str__(self):
        return super().__str__() + f", type_of_sport={self.type_of_sport}"

    def to_dict(self):
        d = super().to_dict()
        d["type"] = "Sport"
        d["type_of_sport"] = self.type_of_sport
        return d

    @staticmethod
    def from_dict(data):
        return Sport(data["product_id"], data["name"], data["price"], data["quantity"], data["type_of_sport"])

class Stationary(Physical_product):
    def __init__(self, product_id, name: str, price: float, quantity: int):
        super().__init__(product_id, name, price, quantity)

    def to_dict(self):
        d = super().to_dict()
        d["type"] = "Stationary"
        return d

    @staticmethod
    def from_dict(data):
        return Stationary(data["product_id"], data["name"], data["price"], data["quantity"])

class Hardware(Physical_product):
    def __init__(self, product_id, name: str, price: float, quantity: int, type_of_hardware: str):
        super().__init__(product_id, name, price, quantity)
        self.type_of_hardware = type_of_hardware

    def __str__(self):
        return super().__str__() + f", type_of_hardware={self.type_of_hardware}"

    def to_dict(self):
        d = super().to_dict()
        d["type"] = "Hardware"
        d["type_of_hardware"] = self.type_of_hardware
        return d

    @staticmethod
    def from_dict(data):
        return Hardware(data["product_id"], data["name"], data["price"], data["quantity"], data["type_of_hardware"])

# Subclasses of Digital_product

class Software(Digital_product):
    def __init__(self, product_id, name: str, price: float, quantity: int, license_key: str):
        super().__init__(product_id, name, price, quantity)
        self.license_key = license_key

    def __str__(self):
        return super().__str__() + f", license_key={self.license_key}"

    def to_dict(self):
        d = super().to_dict()
        d["type"] = "Software"
        d["license_key"] = self.license_key
        return d

    @staticmethod
    def from_dict(data):
        return Software(data["product_id"], data["name"], data["price"], data["quantity"], data["license_key"])

class Ebook(Digital_product):
    def __init__(self, product_id, name: str, price: float, quantity: int, author: str):
        super().__init__(product_id, name, price, quantity)
        self.author = author

    def __str__(self):
        return super().__str__() + f", author={self.author}"

    def to_dict(self):
        d = super().to_dict()
        d["type"] = "Ebook"
        d["author"] = self.author
        return d

    @staticmethod
    def from_dict(data):
        return Ebook(data["product_id"], data["name"], data["price"], data["quantity"], data["author"])

class Service(Digital_product):
    def __init__(self, product_id, name: str, price: float, quantity: int, duration: str):
        super().__init__(product_id, name, price, quantity)
        self.duration = duration

    def __str__(self):
        return super().__str__() + f", duration={self.duration}"

    def to_dict(self):
        d = super().to_dict()
        d["type"] = "Service"
        d["duration"] = self.duration
        return d

    @staticmethod
    def from_dict(data):
        return Service(data["product_id"], data["name"], data["price"], data["quantity"], data["duration"])

class MusicProduct(Digital_product):
    def __init__(self, product_id, name: str, price: float, quantity: int, artist: str, album: str, duration: str, audio_format: str):
        super().__init__(product_id, name, price, quantity)
        self.artist = artist
        self.album = album
        self.duration = duration
        self.audio_format = audio_format

    def __str__(self):
        return super().__str__() + f", artist={self.artist}, album={self.album}, duration={self.duration}, audio_format={self.audio_format}"

    def to_dict(self):
        d = super().to_dict()
        d["type"] = "MusicProduct"
        d["artist"] = self.artist
        d["album"] = self.album
        d["duration"] = self.duration
        d["audio_format"] = self.audio_format
        return d

    @staticmethod
    def from_dict(data):
        return MusicProduct(data["product_id"], data["name"], data["price"], data["quantity"], data["artist"], data["album"], data["duration"], data["audio_format"])