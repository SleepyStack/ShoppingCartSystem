import json
import os
from product import Product, PhysicalProduct, DigitalProduct
from cart_item import CartItem

class ShoppingCart:
    def __init__(self, product_catalog_file='products.json', cart_state_file='cart.json'):
        self._items = {}  # product_id: CartItem
        self._product_catalog_file = product_catalog_file
        self._cart_state_file = cart_state_file
        self.catalog = self._load_catalog()
        self._load_cart_state()

    def _load_catalog(self):
        catalog = {}
        if not os.path.exists(self._product_catalog_file):
            return catalog
        try:
            with open(self._product_catalog_file, 'r') as f:
                products_data = json.load(f)
            for p in products_data:
                typ = p.get('type', 'product')
                if typ == 'physical':
                    product = PhysicalProduct(
                        p['product_id'], p['name'], p['price'], p['quantity_available'], p['weight']
                    )
                elif typ == 'digital':
                    product = DigitalProduct(
                        p['product_id'], p['name'], p['price'], p['quantity_available'], p['download_link']
                    )
                else:
                    product = Product(
                        p['product_id'], p['name'], p['price'], p['quantity_available']
                    )
                catalog[product.product_id] = product
        except Exception as e:
            print(f"Error loading catalog: {e}")
        return catalog

    def _save_catalog(self, catalog=None):
        if catalog is None:
            catalog = self.catalog
        data = [p.to_dict() for p in catalog.values()]
        try:
            with open(self._product_catalog_file, 'w') as f:
                json.dump(data, f, indent=2)
        except Exception as e:
            print(f"Error saving catalog: {e}")

    def _load_cart_state(self):
        if not os.path.exists(self._cart_state_file):
            return
        try:
            with open(self._cart_state_file, 'r') as f:
                cart_data = json.load(f)
            for item in cart_data:
                pid = item['product_id']
                if pid in self.catalog:
                    self._items[pid] = CartItem(self.catalog[pid], item['quantity'])
        except Exception as e:
            print(f"Error loading cart state: {e}")

    def _save_cart_state(self):
        data = [item.to_dict() for item in self._items.values()]
        try:
            with open(self._cart_state_file, 'w') as f:
                json.dump(data, f, indent=2)
        except Exception as e:
            print(f"Error saving cart state: {e}")

    def add_item(self, product_id, quantity):
        if product_id not in self.catalog:
            print("Product not found.")
            return False
        product = self.catalog[product_id]
        if quantity < 1 or quantity > product.quantity_available:
            print("Invalid quantity or insufficient stock.")
            return False
        if product_id in self._items:
            cart_item = self._items[product_id]
            if product.quantity_available < quantity:
                print("Not enough stock.")
                return False
            cart_item.quantity += quantity
        else:
            cart_item = CartItem(product, quantity)
            self._items[product_id] = cart_item
        product.decrease_quantity(quantity)
        self._save_cart_state()
        self._save_catalog()
        print(f"Added {quantity} x {product.name} to the cart.")
        return True

    def remove_item(self, product_id):
        if product_id not in self._items:
            print("Item not in the cart.")
            return False
        cart_item = self._items.pop(product_id)
        cart_item.product.increase_quantity(cart_item.quantity)
        self._save_cart_state()
        self._save_catalog()
        print(f"Removed {cart_item.product.name} from the cart.")
        return True

    def update_quantity(self, product_id, new_quantity):
        if product_id not in self._items:
            print("Item not in the cart.")
            return False
        cart_item = self._items[product_id]
        if new_quantity < 0:
            print("Quantity cannot be negative.")
            return False
        diff = new_quantity - cart_item.quantity
        if diff > 0:
            if cart_item.product.quantity_available < diff:
                print("Not enough stock to increase quantity.")
                return False
            cart_item.product.decrease_quantity(diff)
        else:
            cart_item.product.increase_quantity(-diff)
        cart_item.quantity = new_quantity
        if new_quantity == 0:
            self._items.pop(product_id)
            print(f"Removed {cart_item.product.name} from the cart.")
        self._save_cart_state()
        self._save_catalog()
        print("Cart updated.")
        return True

    def get_total(self):
        return sum(item.calculate_subtotal() for item in self._items.values())

    def display_cart(self):
        if not self._items:
            print("Your cart is empty.")
            return
        print("\nYour Cart:")
        print("-" * 60)
        for item in self._items.values():
            print(item)
        print("-" * 60)
        print(f"Grand Total: ${self.get_total():.2f}")

    def display_products(self):
        if not self.catalog:
            print("No products available.")
            return
        print("\nAvailable Products:")
        print("-" * 60)
        for product in self.catalog.values():
            print(product.display_details())
        print("-" * 60)