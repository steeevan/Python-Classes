#Assignment 1
def square_number(Tnumber):
    Tnumber **= 2
    return Tnumber

s = square_number(5)

print(s)

def calculate_average(a,b,c):
    s = a + b + c

    s /= 3
    return s

c = calculate_average(3,6,1)

print(c)

def print_greeting():
    name = input("What is your name? ")

    print(f"Hello {name}!")
print_greeting()

#Assignment 2
try:
    number1 = int(input("What is the first number you want to divide? "))
    number2 = int(input("What is the second number you want to use to divide the first number? "))

    result = number1 / number2

    print(result)
except ZeroDivisionError:
    print("The second number cannot be zero.")

try:
    age = int(input("What is your age? "))
except ValueError:
    print("That is not a valid integer.")

#Assignment 3        
def calculate_discount(price,percent):
    discount = price * percent / 100
    return price - discount
d = calculate_discount(761,33)

print(d)


def convert_tempature(celsius):
    Fahrenheit = celsius * 1.8 + 32
    return Fahrenheit
c = convert_tempature(13)

print(c)
    
#Assignment 4
#I don't know





 
