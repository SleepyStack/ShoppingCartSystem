from dataclasses import dataclass, asdict
from typing import Dict, Any, Type

@dataclass
class Product:
    product_id: int
    name: str
    price: float
    quantity: int

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Product":
        product_type = data.get("type", "Product")
        return PRODUCT_TYPES.get(product_type, Product)._from_dict(data)

    @classmethod
    def _from_dict(cls, data):
        return cls(
            product_id=data["product_id"],
            name=data["name"],
            price=data["price"],
            quantity=data["quantity"]
        )

    def to_dict(self) -> dict:
        d = asdict(self)
        d["type"] = self.__class__.__name__
        return d

    def decrease_quantity(self, amount: int):
        if amount > self.quantity:
            raise ValueError("Not enough stock.")
        self.quantity -= amount

    def increase_quantity(self, amount: int):
        self.quantity += amount

# Example subclass for a Grocery item
@dataclass
class Grocery(Product):
    expiration_date: str = ""

    @classmethod
    def _from_dict(cls, data):
        return cls(
            product_id=data["product_id"],
            name=data["name"],
            price=data["price"],
            quantity=data["quantity"],
            expiration_date=data.get("expiration_date", "")
        )

    def to_dict(self) -> dict:
        d = super().to_dict()
        d["expiration_date"] = self.expiration_date
        return d

@dataclass
class Software(Product):
    license_key: str = ""

    @classmethod
    def _from_dict(cls, data):
        return cls(
            product_id=data["product_id"],
            name=data["name"],
            price=data["price"],
            quantity=data["quantity"],
            license_key=data.get("license_key", "")
        )

    def to_dict(self) -> dict:
        d = super().to_dict()
        d["license_key"] = self.license_key
        return d

@dataclass
class Clothing(Product):
    size: str = ""
    color: str = ""

    @classmethod
    def _from_dict(cls, data):
        return cls(
            product_id=data["product_id"],
            name=data["name"],
            price=data["price"],
            quantity=data["quantity"],
            size=data.get("size", ""),
            color=data.get("color", "")
        )

    def to_dict(self) -> dict:
        d = super().to_dict()
        d["size"] = self.size
        d["color"] = self.color
        return d

PRODUCT_TYPES: Dict[str, Type[Product]] = {
    "Product": Product,
    "Grocery": Grocery,
    "Clothing": Clothing,
    "Software": Software,
}