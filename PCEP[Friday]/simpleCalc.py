def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b


def main_menu():
    print("Simple Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

while True:
    main_menu()
    choice = input("Enter your choice: ")
    if choice in ["1", "2", "3", "4"]:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
            print("Result:", add(num1, num2))
        elif choice == "2":
            print("Result:", subtract(num1, num2))
        elif choice == "3":
            print("Result:", multiply(num1, num2))
        elif choice == "4":
            print("Result:", divide(num1, num2))
    elif choice == "5":
        break
    else:
        print("Invalid choice, please try again.")
