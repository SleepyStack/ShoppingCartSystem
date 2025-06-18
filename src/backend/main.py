from inventory import Inventory
from cart import Cart

def find_product_by_id_or_name(inventory, query):
    if isinstance(query, int) and query in inventory:
        return inventory[query]
    for product in inventory.values():
        if product.name.lower() == str(query).lower():
            return product
    return None

def main():
    inventory = Inventory.inventory
    cart = Cart()

    while True:
        action = input("Enter 'add' to add to cart, 'view' to see cart, 'checkout' to finish, or 'exit': ").strip().lower()
        if action == 'add':
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
        elif action == 'view':
            cart.view_cart(inventory)
        elif action == 'checkout':
            cart.checkout(inventory)
            cart.items.clear()  # Optional: Clear cart after checkout
            break
        elif action == 'exit':
            break
        else:
            print("Invalid action.")

if __name__ == "__main__":
    main()