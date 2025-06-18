import json
import os
from typing import Dict
from product import Product

class Inventory:
    def __init__(self, filename="products.json"):
        # Always load products.json from the same directory as this file
        self.filename = os.path.join(os.path.dirname(__file__), filename)
        self.products: Dict[int, Product] = {}
        self.load()

    def load(self):
        try:
            with open(self.filename, "r") as f:
                data = json.load(f)
            self.products = {d["product_id"]: Product.from_dict(d) for d in data}
        except FileNotFoundError:
            self.products = {}

    def save(self):
        with open(self.filename, "w") as f:
            json.dump([p.to_dict() for p in self.products.values()], f, indent=2)

    def get(self, product_id: int) -> Product:
        return self.products.get(product_id)