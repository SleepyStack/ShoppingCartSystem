from inventory import Inventory
from cart import ShoppingCart

def main_menu():
    inventory = Inventory()
    cart = ShoppingCart(inventory)
    while True:
        print("\n1. View Products\n2. Add to Cart\n3. View Cart\n4. Update Quantity\n5. Remove from Cart\n6. Checkout (dummy)\n7. Exit")
        choice = input("Choice: ")
        if choice == "1":
            # Print table header
            print("\n{:<5} {:<20} {:<10} {:<8} {:<12} {:<12} {:<20}".format(
                "ID", "Name", "Type", "Price", "Stock", "Size/Expiry", "Color/License"
            ))
            print("-" * 90)
            for p in inventory.products.values():
                ptype = type(p).__name__
                size_or_exp = ""
                color_or_lic = ""
                if ptype == "Grocery":
                    size_or_exp = getattr(p, "expiration_date", "")
                elif ptype == "Clothing":
                    size_or_exp = getattr(p, "size", "")
                    color_or_lic = getattr(p, "color", "")
                elif ptype == "Software":
                    color_or_lic = getattr(p, "license_key", "")
                print("{:<5} {:<20} {:<10} ${:<7.2f} {:<8} {:<12} {:<20}".format(
                    p.product_id, p.name, ptype, p.price, p.quantity, size_or_exp, color_or_lic
                ))
        elif choice == "2":
            pid = int(input("Product ID: "))
            qty = int(input("Quantity: "))
            try:
                cart.add(pid, qty)
                print("Added to cart.")
            except Exception as e:
                print(e)
        elif choice == "3":
            for item in cart.items.values():
                print(f"{item.product.name}: {item.quantity} x ${item.product.price:.2f} = ${item.subtotal():.2f}")
            print(f"Total: ${cart.total():.2f}")
        elif choice == "4":
            pid = int(input("Product ID: "))
            qty = int(input("New quantity: "))
            try:
                cart.update(pid, qty)
                print("Updated.")
            except Exception as e:
                print(e)
        elif choice == "5":
            pid = int(input("Product ID: "))
            cart.remove(pid)
            print("Removed.")
        elif choice == "6":
            print("Checkout not implemented.")
        elif choice == "7":
            break
        else:
            print("Invalid.")