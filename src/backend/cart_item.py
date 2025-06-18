class CartItem:
    def __init__(self, product, quantity: int):
        self._product = product
        self._quantity = quantity

    @property
    def product(self):
        return self._product

    @property
    def quantity(self):
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        if value < 0:
            raise ValueError("Quantity in cart cannot be negative.")
        self._quantity = value

    def calculate_subtotal(self) -> float:
        return self.product.price * self.quantity

    def __str__(self):
        return f"Item: {self.product.name}, Quantity: {self.quantity}, Price: ${self.product.price:.2f}, Subtotal: ${self.calculate_subtotal():.2f}"

    def to_dict(self) -> dict:
        return {
            "product_id": self.product.product_id,
            "quantity": self.quantity
        }