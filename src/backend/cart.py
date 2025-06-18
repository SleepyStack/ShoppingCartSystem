class Cart:
    def __init__(self):
        self.items = {}  # key: product_id, value: quantity

    def add_item(self, product, quantity):
        if product.product_id in self.items:
            self.items[product.product_id] += quantity
        else:
            self.items[product.product_id] = quantity

    def remove_item(self, product, quantity):
        if product.product_id in self.items:
            self.items[product.product_id] -= quantity
            if self.items[product.product_id] <= 0:
                del self.items[product.product_id]
        else:
            print(f"{product.name} not in cart.")

    def view_cart(self, inventory):
        print("\nYour Cart:")
        total = 0
        for product_id, quantity in self.items.items():
            product = inventory.get(product_id)
            if not product:
                print(f"Product with ID {product_id} not found in inventory!")
                continue
            item_total = product.price * quantity
            total += item_total
            print(f"{product.name:25} | ${product.price:.2f} × {quantity} = ${item_total:.2f}")
        print("-" * 50)
        print(f"Total: ${total:.2f}\n")
        return total

    def checkout(self, inventory):
        total = self.view_cart(inventory)
        print(f"Proceeding to checkout. Total amount due: ${total:.2f}")
        return total