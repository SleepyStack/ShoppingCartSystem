import json
from typing import Dict
from cart_item import CartItem
from product import Product
from inventory import Inventory

class ShoppingCart:
    def __init__(self, inventory: Inventory, cart_file="cart.json"):
        self.inventory = inventory
        self.cart_file = cart_file
        self.items: Dict[int, CartItem] = {}
        self.load()

    def add(self, product_id: int, quantity: int):
        product = self.inventory.get(product_id)
        if not product:
            raise ValueError("Product does not exist.")
        if quantity > product.quantity:
            raise ValueError("Not enough stock.")
        if product_id in self.items:
            self.items[product_id].quantity += quantity
        else:
            self.items[product_id] = CartItem(product, quantity)
        product.decrease_quantity(quantity)
        self.save()
        self.inventory.save()

    def remove(self, product_id: int):
        if product_id in self.items:
            item = self.items.pop(product_id)
            item.product.increase_quantity(item.quantity)
            self.save()
            self.inventory.save()

    def update(self, product_id: int, quantity: int):
        if product_id not in self.items:
            raise ValueError("Item not in cart.")
        item = self.items[product_id]
        diff = quantity - item.quantity
        if diff > 0:
            if diff > item.product.quantity:
                raise ValueError("Not enough stock.")
            item.product.decrease_quantity(diff)
        else:
            item.product.increase_quantity(-diff)
        item.quantity = quantity
        if item.quantity == 0:
            self.items.pop(product_id)
        self.save()
        self.inventory.save()

    def total(self) -> float:
        return sum(item.subtotal() for item in self.items.values())

    def save(self):
        with open(self.cart_file, "w") as f:
            json.dump([item.to_dict() for item in self.items.values()], f, indent=2)

    def load(self):
        try:
            with open(self.cart_file, "r") as f:
                data = json.load(f)
            for d in data:
                product = self.inventory.get(d["product_id"])
                if product:
                    self.items[product.product_id] = CartItem(product, d["quantity"])
        except FileNotFoundError:
            self.items = {}