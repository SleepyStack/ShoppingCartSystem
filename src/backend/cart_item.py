from product import Product

class CartItem:
    def __init__(self, product: Product, quantity: int):
        self.product = product
        self.quantity = quantity

    def subtotal(self) -> float:
        return self.product.price * self.quantity

    def to_dict(self):
        return {
            "product_id": self.product.product_id,
            "quantity": self.quantity
        }