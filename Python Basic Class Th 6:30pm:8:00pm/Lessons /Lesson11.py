# ===============================================
# Lesson Plan: Functions in Python
# ===============================================

# **Objective:** Introduce functions, arguments, parameters, and return statements in Python.

# ===============================================
# 1. Introduction to Functions
# ===============================================
# Functions are reusable blocks of code that performs a specific task.
# They allow you to organize and modularize your code for better
# readability and maintanability.

# ===============================================
# 2. Defining Functions
# ========================================= ======

# Functions are defined using the "def" keyword, followed by the
#function name and a pair of parentheses.

def greet():
  print("Hello World")
  print("Welcome to my Class")
  print("I am learning about functions today!")
  
  # ===============================================
# 3. Calling Functions (Invocate)
# ===============================================

# Functions are executed by calling their names followed by parentheses.

greet()

# ===============================================
# 4. Parameters and Arguments
# ===============================================

# Functions can take parameters (input values) and arguments are 
# the actual values passed to the function.


def greet_user(username):
  print(f"Hello, {username}!")
  
  

greet_user("Estevan")


# ===============================================
# 5. Return Statements
# ===============================================

# Functions can return values using the "return" statement.
 
def add_numbers(num1, num2):
  result = num1 + num2
  return result
  
sum_result = add_numbers(3.0,5.5)

print(f"Sum: {sum_result}")


# ===============================================
# 6. Scope of Variables
# ===============================================

# Variables defined inside a function have local scope and are only 
# accessible within that function.
# Variables defined outside functions have global scope and can be 
# accessed from anywhere in the program.

variable = 10

def local_scope_example():
  local_variable = 20
  print(f"Local variable: {local_variable}")
  print(f"Globa variable(inside function): {variable}")
  
  
local_scope_example()
print("Global variable (outside funtion): ", variable)








# Example 1 Function default parameters
def greet_person(name = "person"):
  print(f"Hello {name}")


greet_person("Estevan")
greet_person()

# Example 2 function with multiple return values
def split_name(full_name):
  firstN, lastN = full_name.split()
  return firstN, lastN

user_input = input("Enter your full name: ")
fn, ln = split_name(user_input)

print(fn,ln)

# Example 3 Recursive function
def factorial(n):
  if n == 0:
    return 1
  else:
    return n * factorial(n-1)


value = factorial(5)
print(value)


# Exercise 1: Write a function that takes two numbers 
# as arguments and returns their product.

def product(num1,num2):
  return num1 * num2

x = product(123215,5)
print(x)




# Exercise 2: Create a function that calculates and returns the area of a rectangle given its length and width.
# Exercise 3: Implement a recursive function to calculate the nth Fibonacci number.

# ===============================================
# 9. Conclusion
# ===============================================

# In this lesson, you've learned about functions, how to define and call them, use parameters and arguments, and return values using the "return" statement. Functions are essential for modularizing code and improving code reusability.

# Continue practicing functions to enhance your programming skills in Python.

# ===============================================
# Vocabulary Words and Definitions
# ===============================================

# - Function: A reusable block of code that performs a specific task.
# - Parameter: A variable used in a function's definition to accept arguments.
# - Argument: The actual value passed to a function when it is called.
# - Return Statement: A statement used in a function to return a value to the caller.
# - Scope: The region of code where a variable can be accessed and manipulated.
# - Local Scope: The scope in which a variable is limited to the function it is defined in.
# - Global Scope: The scope in which a variable can be accessed from anywhere in the program.




















