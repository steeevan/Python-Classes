#1-2

def greet_user(name):
  print (f"Welcome to coding class, {name}")
greet_user(name=input("What's your name?"))

def square_number(number):
  print (f"Your number: {number}")
  print (f"Your number squared:", number**2)
square_number(number=int(input("Enter a number")))

#3-4

def calculate_area(l, w):
  print (f"Area of this rectange: {l*w}")
calculate_area(l=int(input("Length of rectangle:")), w=int(input("Width of rectangle:")))
#for #4, enter 5 for length and 3 for width because I am using input

#5-6
def divide_numbers(fn, sn):
  print (f"{fn} divided by {sn} equals {round(fn/sn)}, with a remainder of {fn%sn}.")
divide_numbers(fn=int(input("Enter a number")), sn=int(input("enter a second number")))

#7-8

def calculate_sum(a, b, c):
  print (f"added together: {a+b+c}")
calculate_sum(a=5, b=10, c=15)

#9-10

def factorial(t):
  if t==0:
    return 1
  else:
    return t * factorial(t-1)
afro=factorial(int(input("Enter number for factorial")))
print(f"factorial: {afro}")

afro2=factorial(4)
print (f"Factorial of 4: {afro2}")
