# ===============================================
# Lesson Plan: Variables and Data Types in Python
# ===============================================

# **Objective:** Introduce the concept of variables and explore different
# data types in Python, such as integers, strings, floats, and booleans.

# ===============================================
# 1. Introduction to Variables
# ===============================================

# Variables are like containers/box that can store different types of data.
# They help us work with information in our program.

# ===============================================
# 2. Naming Variables
# ===============================================

#Valid Variable Names
# - Must start with a letter (a-z, A-Z) or an underscore(_)
# ex. 'my_variable', '_variable1', 'Name'
# - Can contain letters, numbers(0-9) or underscores
# ex. 'My_var_var_123', name123456789'
# Variables are case-sensitive
# ex. 'myVariable' , 'MyVariable', myvariable'
# there are all different variables
# - Cannot be usign a reserved keyworkd in Python
# ex. if, else, for, def, return, etc.


# Invalid Variables
# - Cannont start with a number
# ex. INVALID: '2variable', '123'
# - Cannot contain any special character(except underscore)
# ex. 'my-variable', 'my@variable', ' my!variable'
# - cannot contain spaces
# ex. 'my variable', 'myVariable I like'



# Example 1

# initialize a variable and set it to 42
my_variable = 42

#initiliaze a variable named [INTEGER] 'name' and set it to your own name
name = "Estevan"
# Initialize a variable named [Boolean]' is_student' and set to true
is_student = True
# Initialize a variable named [float] 'temperature' and set it to 25.5
temperature = 25.5

# print all 4 values
print("I chose ",my_variable, " and my name is ",name)
print("Am i a student? ",is_student)
print("Today it is ", temperature, " degrees C.")
print()


# Exercise 2
# Ask the user to enter two INTEGER
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a new number: "))

# Getting sum of num1 and num2
my_sum = num1 + num2

print("My sum is: ",my_sum)


# Get the difference of num1 and num2
# assign the difference to 'my_diff'
#print it out
my_diff = num1 - num2

print("My difference is: ",my_diff)

# Get the product of num1 and num2
# assign the product to 'my_prod'
#print it out
my_prod = num1 * num2

print("My product is: ",my_prod)

# Get the quotient of num1 and num2
# assign the quotient to 'my_quo'
#print it out
my_quo = num1 / num2

print("My Quotient is: ",my_quo)


















