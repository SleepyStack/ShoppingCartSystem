from cart import ShoppingCart

def main_menu():
    cart = ShoppingCart()
    while True:
        print("""
========= Shopping Cart Menu =========
1. View Products
2. Add Item to Cart
3. View Cart
4. Update Cart Item Quantity
5. Remove Item from Cart
6. Checkout (dummy)
7. Exit
""")
        choice = input("Enter your choice: ")
        if choice == "1":
            cart.display_products()
        elif choice == "2":
            pid = input("Enter Product ID to add: ")
            qty = int(input("Enter quantity: "))
            cart.add_item(pid, qty)
        elif choice == "3":
            cart.display_cart()
        elif choice == "4":
            pid = input("Enter Product ID to update: ")
            qty = int(input("Enter new quantity: "))
            cart.update_quantity(pid, qty)
        elif choice == "5":
            pid = input("Enter Product ID to remove: ")
            cart.remove_item(pid)
        elif choice == "6":
            print("Checkout complete. (Not implemented)")
        elif choice == "7":
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")