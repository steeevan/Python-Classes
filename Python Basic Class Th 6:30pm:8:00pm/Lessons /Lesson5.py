# ===============================================
# Lesson Plan: Conditional Statements (if, elif, else) in Python
# ===============================================


# **Objective:** Introduce conditional statements for decision-making in Python.


# ===============================================
# 1. Introduction to Conditional Statements
# ===============================================

# Conditional statements allow us to make decisions in our programs. 
# They help us execute different code blocks based on specified conditions.

# ===============================================
# 2. The "if" Statement
# ===============================================

# tHE "if" statements is used to execute a block of code if a condition is True.

#example 1
age = 20

if age >= 18:
  print("You are an adult")

# example 2
word = "Python"

if word == "Python":
  print("You are learning ", word)
  

# ===============================================
# 3. The "elif" Statement
# ===============================================

# The "elif" (short for "else if") statement is used to specify multiple 
# conditions to check.


# Example 1
temp = 40

if temp > 30:
  print("Its hot outsude")
elif temp >= 25:
  print("Its pleasent")
  
  

# ===============================================
# 4. The "else" Statement
# ===============================================

# The "else" statement is used to execute a block of code 
# if the condition specified in the "if" statement is False.
  
# Example 1

num = 8
if num % 2 == 0:
  print("even")
else:
  print("odd")


# ===============================================
# 5. Nested Conditional Statements
# ===============================================

# Conditional statements can be nested inside each other to handle 
# more complex situations.


# Example 1
x = 11
y = 5
if x > y:
  
  if x % 2 == 0:
    print("x is greater and even")
  else:
    print("x is greater and odd")
    
else:
  print("y is greater")


# Class Exercises
# Basic Calculator

num1 = float(input("Enter a number: "))
num2 = float(input("Enter a second number: "))
operator = input("Enter a operator (+, -, *, / ): ")

'''
print("Number 1: ",num1)
print("Number 2: ",num2)
print("Youe equation: ",num1, operator, num2)

'''

if operator == '+':
  result = num1 + num2
  print("Youe equation: ",num1, operator, num2, " = ", result)
elif operator == '-':
  result = num1 - num2
  print("Youe equation: ",num1, operator, num2, " = ", result)
elif operator == '*':
  result = num1 * num2
  print("Youe equation: ",num1, operator, num2, " = ", result)
elif operator == '/':
  if num2 == 0:
    print("Error! Division by Zero is not possible.")
  else:
    result = num1 / num2
    print("Youe equation: ",num1, operator, num2, " = ", result)
else:
  print("You did not pick a valid operator!")



# ===============================================
# 7. Conclusion
# ===============================================

# In this lesson, you've learned about conditional statements in Python, including
# the "if," "elif," and "else" statements. These statements enable you to make decisions
# and execute specific code blocks based on conditions.

# Practice using conditional statements to control the flow of your
#programs and make them more dynamic and responsive.

# ===============================================
# Vocabulary Words and Definitions
# ===============================================

# - Conditional Statements: Statements that allow different code blocks to be executed
# based on specified conditions.

# - "if" Statement: A conditional statement used to execute a block of code
# if a condition is True.

# - "elif" Statement: A conditional statement used to specify multiple conditions 
# to check after the initial "if" statement.

# - "else" Statement: A conditional statement used to execute a block of code 
# if the condition in the "if" statement is False.

# - Nested: Placing one construct (e.g., conditional statement) inside another 
# construct of the same kind.








