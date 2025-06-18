import json
from product import Product

class Inventory:
    def __init__(self, filename="products.json"):
        self.filename = filename
        self.inventory = self.load_inventory()

    def load_inventory(self):
        try:
            with open(self.filename, "r") as f:
                data = json.load(f)
            inv = {}
            for item in data:
                product = Product.from_dict(item)
                inv[product.product_id] = product
            return inv
        except FileNotFoundError:
            print("[INFO] Inventory file not found. Starting with empty inventory.")
            return {}
        except Exception as e:
            print(f"[ERROR] Failed to load inventory: {e}")
            return {}

    def save_inventory(self):
        try:
            with open(self.filename, "w") as f:
                json.dump([p.to_dict() for p in self.inventory.values()], f, indent=2)
        except Exception as e:
            print(f"[ERROR] Failed to save inventory: {e}")