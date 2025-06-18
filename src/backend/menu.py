from cart import Cart
from inventory import Inventory

def find_product_by_id_or_name(inventory, query):
    if isinstance(query, int) and query in inventory:
        return inventory[query]
    for product in inventory.values():
        if product.name.lower() == str(query).lower():
            return product
    return None

def show_inventory(inventory):
    print("\nAvailable Products:")
    print("-" * 80)
    for product in inventory.values():
        print(f"[{product.product_id}] {product.name:30} | ${product.price:.2f} | In stock: {product.quantity}")
    print("-" * 80)

def cart_menu(cart, inventory):
    while True:
        print("\nCart Menu:")
        print("1. Add to cart")
        print("2. Remove from cart")
        print("3. View cart")
        print("4. Checkout")
        print("5. Back to main menu")
        choice = input("Choose an option: ").strip()
        if choice == '1':
            query = input("Enter product serial number or name: ").strip()
            try:
                query_int = int(query)
                query = query_int
            except ValueError:
                pass
            product = find_product_by_id_or_name(inventory, query)
            if product:
                try:
                    quantity = int(input(f"Enter quantity for {product.name}: "))
                except ValueError:
                    print("Invalid quantity! Please enter a number.")
                    continue
                if quantity > product.quantity:
                    print("Not enough stock!")
                elif quantity <= 0:
                    print("Please enter a positive quantity.")
                else:
                    cart.add_item(product, quantity)
                    product.quantity -= quantity  # Decrement stock here
                    print(f"Added {quantity} of {product.name} to cart.")
            else:
                print("Product not found.")
        elif choice == '2':
            query = input("Enter product serial number or name to remove: ").strip()
            try:
                query_int = int(query)
                query = query_int
            except ValueError:
                pass
            product = find_product_by_id_or_name(inventory, query)
            if product and product.product_id in cart.items:
                try:
                    quantity = int(input(f"Enter quantity to remove for {product.name}: "))
                except ValueError:
                    print("Invalid quantity! Please enter a number.")
                    continue
                cart.remove_item(product, quantity)
                product.quantity += quantity  # Restock
                print(f"Removed {quantity} of {product.name} from cart.")
            else:
                print("Product not found in cart.")
        elif choice == '3':
            cart.view_cart(inventory)
        elif choice == '4':
            cart.checkout(inventory)
            cart.items.clear()
            break
        elif choice == '5':
            break
        else:
            print("Invalid action.")

def main_menu():
    inventory = Inventory.inventory
    cart = Cart()

    while True:
        print("\nMain Menu:")
        print("1. View Inventory")
        print("2. Go to Cart")
        print("3. Exit")
        menu_choice = input("Choose an option: ").strip()
        if menu_choice == '1':
            show_inventory(inventory)
        elif menu_choice == '2':
            cart_menu(cart, inventory)
        elif menu_choice == '3':
            print("Thank you for using the Shopping Cart System. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")