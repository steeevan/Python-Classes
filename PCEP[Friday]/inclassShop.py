import random

def load_items():
    items = {
        "apple": 0.5,
        "banana": 0.3,
        "bread": 2.0,
        "milk": 1.5,
        "cheese": 2.5,
        "chocolate": 1.0
    }
    
    return items

def list_items(items):
    print("Available Items:")
    for item, price in items.items():
        print(f"{item.capitalize()}: ${price:.2f}")
    print()

def add_to_cart(cart,items):
    item = input("Enter the name of the item to add to the cart: ").lower()
    if item in items:
        quantity = int(input("Enter the quantatiy: "))
        if item in cart:
            cart[item] += quantity
        else:
            cart[item] = quantity
        print(f"Added {quantity} {item}(s) to the cart.\n")
    else:
        print("Item not found")



def remove_from_cart(cart):
    item = input("Enter the name of the item to remove from the cart: ").lower()
    if item in cart:
        quantity = int(input("Enter the quantity to remove: "))
        if quantity >= cart[item]:
            del cart[item]
        else:
            cart[item] -= quantity
        print(f"Removed {quantity} {item}(s) from the cart.\n")
    else:
        print("Item not found in the cart.\n")
def view_cart(cart):
    if not cart:
        print("The cart is empty.\n")
    else:
        print("Shopping Cart:")
        for item, quantity in cart.items():
            print(f"{item.capitalize()}: {quantity}")
        print()

def checkout(cart, items):
    if not cart:
        print("The cart is empty. Nothing to checkout.\n")
        return

    total = sum(items[item] * quantity for item, quantity in cart.items())
    discount = random.randint(5, 20)
    discounted_total = total - (total * discount / 100)

    print("Checking out...")
    print(f"Total: ${total:.2f}")
    print(f"Discount: {discount}%")
    print(f"Total after discount: ${discounted_total:.2f}\n")


