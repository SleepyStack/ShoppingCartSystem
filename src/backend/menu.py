from inventory import Inventory
from cart import Cart

def main_menu():
    inventory = Inventory()
    cart = Cart()
    while True:
        print("""
========= Shopping Cart Menu =========
1. View Products
2. Add Item to Cart
3. View Cart
4. Remove Item from Cart
5. Checkout (dummy)
6. Exit
""")
        choice = input("Enter your choice: ")
        if choice == "1":
            print("\nAvailable Products:")
            for product in inventory.inventory.values():
                print(product)
        elif choice == "2":
            product_id = input("Enter Product ID to add: ")
            try:
                product_id = int(product_id)
                product = inventory.inventory.get(product_id)
                if not product:
                    print("Product not found.")
                    continue
                quantity = int(input("Enter quantity: "))
                if quantity < 1 or quantity > product.quantity:
                    print("Invalid quantity.")
                    continue
                cart.add_item(product, quantity)
                product.quantity -= quantity
                print(f"Added {quantity} x {product.name} to cart.")
            except Exception as e:
                print(f"Error: {e}")
        elif choice == "3":
            cart.view_cart(inventory.inventory)
        elif choice == "4":
            product_id = input("Enter Product ID to remove: ")
            try:
                product_id = int(product_id)
                product = inventory.inventory.get(product_id)
                if not product:
                    print("Product not found.")
                    continue
                quantity = int(input("Enter quantity to remove: "))
                if quantity < 1 or product_id not in cart.items:
                    print("Invalid quantity or product not in cart.")
                    continue
                cart.remove_item(product, quantity)
                product.quantity += quantity
                print(f"Removed {quantity} x {product.name} from cart.")
            except Exception as e:
                print(f"Error: {e}")
        elif choice == "5":
            cart.checkout(inventory.inventory)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")