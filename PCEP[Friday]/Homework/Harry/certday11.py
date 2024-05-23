import time
import random
cart = {"key": None,"quantity": 0}
def load_items():
    items = {
        "apple": 0.5,
        "banana": 0.5,

        "bread": 0.52,
        "milk": 1.5,

        "cheese": 0.5,
        
    }
    return items

def main_menu():
    time.sleep(0.5)
    print("Welcome to the grocery store.")
    time.sleep(2)
    print("1. View store items\n2. Add store items to shopping cart \n3. Remove Item(s)\n4. View cart\n5. Checkout\n6.Quit application")
    input1 = int(input("Enter a choice: "))
    store = load_items()
    if input1 == 1:
        print("Showing items")
        list_items(store)
        print(store)
    if input1 == 2:
        add_to_cart(cart,store)
    if input1 ==3:
        remove_items(cart)
    if input1 ==4:
        view_cart(cart)
    if input1 == 5:
        checkout(cart,store)
    if input1 == 6:
        print("Quitting application")
        quit()
        



def list_items(items):
    print("Availiable items:")
    for items,price in items.items():
        print(f"{items.capitalize()}: ${price:.2f}")
    print("Taking you back to the menu in 5 seconds")
    time.sleep(5)

    main_menu()

def add_to_cart(cart, items):
    On_input =  input("Which item you want to add: ").lower()

    
    if On_input in items:
        try:
            quanitity = int(input("How much items you want: "))
            

            if On_input in cart:
                
                cart[On_input] += quanitity
            else:
                cart[On_input] = quanitity
            print(f"Added {quanitity} {On_input} (s) to the cart . \n ")
            main_menu()
        except ValueError:
            print("ERR \nreturing back to menu soon")
            main_menu()
    else:
        print("Item does not exist")
        time.sleep(2)
        main_menu()
def remove_items(cart):
    remove_item = input("Which item you want to remove ->: ").lower()
    if remove_item in cart:
        quanitity = int(input("How much items you want to remove ->: "))
        if quanitity >= cart[remove_item]:
            del cart[remove_item]
        else:
            cart[remove_item] -= quanitity
        print(f"Removed {quanitity} {remove_item}(s) from the cart.\n")
        main_menu()
    else:
        print("Item does not exist")  
        main_menu()
    
def view_cart(cart):
    if not cart:
        print("The cart is empty.\n")
    else:
        print("Shopping Cart:")
        for item, quantity in cart.items():
            print(f"{item.capitalize()}: {quantity}")
        print()
        print("Teleporting back to menu")
        main_menu()

def checkout(cart,items):
    if not cart:
        print("There is nothing to checkout")
        main_menu()
    print(items.keys())
   
    total = sum(items[item]* quantity for item,quantity in cart.items())
    discount = random.randint(5,20)
    discount_total = total-(total*discount/100)
    print("Checking out...")
    time.sleep(random.randint(0.5,2))
    print(f"Total: {total:2.f}")
    print(f"Discount: {discount}$")
    print(f"Total price after discounted:\n${discount_total}\n")
if __name__ == "__main__":
    
    main_menu()