def square_number(number):
    print(number**2)
square_number(6)

def calculate_average(num1, num2, num3):
    x=num1+num2+num3
    print(x/3)
calculate_average(3,4,5)

def print_greeting():
    y = str(input("What's your name? "))
    print("hi, ",y)

print_greeting()
x = "-----------------------------------------"

print(x)
#problem 2

def Exeption(num4,num5):
    num4 = int(input("enter your first number: "))
    num5 = int(input("enter your second number: "))
    
    try:
        print(num4/num5)  
    except ZeroDivisionError:
        print("Can't divide by 0")
    

Exeption(4,0)

print(x)
#problem 3

def caculate_discount(price, discount):
    price = int(input("What is the price? "))
    discount = int(input("What is the discount percentage? "))

    print(price-price/discount)

caculate_discount(456, 20)

def convert_tempature(celsius):
    celsius = int(input("what is the tempeture in celsius? "))
    print((celsius*9/5)+32," fahrenheit")
convert_tempature(56)

print(x)
#problem 4

def triangle(a,b,c):
    if a==b and a==c:
        print("This is a equilateral triangle")
    elif a==b and a!=c:
        print("This is a Isoceles triangle")
    elif a==c and b!=c:
        print("This is a Isoceles triangle")
    elif b==c and b!=a:
        print("This is a Isoceles triangle")
    elif a!=b and b!=c:
        print("This is a scalene triangle")

triangle(1,3,3)
        




    
    
