# ===============================================
# Lesson Plan: Functions Part 2 in Python
# ===============================================

# **Objective:** Continue working with functions, arguments, parameters, and return statements in Python. Complete exercises and challenges in class.

# ===============================================
# 1. Review of Functions
# ===============================================

# Review the basics of functions, including their definition, parameters, and return statements.

# Example:
def greet_user(name):
    return f"Hello, {name}!"

# ===============================================
# 2. Function Parameters (Default and Keyword)
# ===============================================

# Explore default parameters and keyword arguments in functions.

# Examples:
def greet_with_default(name="User"):
    return f"Hello, {name}!"

def greet_with_keyword_args(first_name, last_name):
    return f"Hello, {first_name} {last_name}!"

# ===============================================
# 3. Variable-Length Argument Lists
# ===============================================

# Learn about using variable-length argument lists in functions.

# Example:
def sum_numbers(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# ===============================================
# 4. Lambda Functions (Anonymous Functions)
# ===============================================

# Introduce lambda functions for creating small, anonymous functions.

# Example:
add = lambda x, y: x + y

# ===============================================
# 5. Recursive Functions
# ===============================================

# Explore recursive functions and their use in solving problems.

# Example:
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# ===============================================
# 6. Exercises and Challenges
# ===============================================

# Exercise 1: Create a function that calculates the average of a list of numbers.
# Exercise 2: Write a function that takes a string and returns the reverse of the string.
# Exercise 3: Implement a function to find the largest element in a list.
# Challenge 1: Write a function to check if a given word is a palindrome.
# Challenge 2: Create a function to compute the nth Fibonacci number without using recursion.

# ===============================================
# 7. Conclusion
# ===============================================

# In this lesson, you've continued to work with functions in Python, exploring default parameters, keyword arguments, variable-length argument lists, lambda functions, and recursive functions. Functions are a powerful tool for solving various programming challenges.

# Continue practicing and exploring advanced concepts to become a more proficient Python programmer.

# ===============================================
# Vocabulary Words and Definitions
# ===============================================

# - Default Parameter: A parameter in a function that has a default value assigned to it.
# - Keyword Argument: An argument in a function call that is specified using the parameter's name.
# - Variable-Length Argument List: A feature in Python that allows a function to accept a variable number of arguments.
# - Lambda Function: An anonymous function defined using the "lambda" keyword.
# - Recursive Function: A function that calls itself as part of its execution.
# - Palindrome: A word, phrase, or sequence that reads the same backward as forward.
# - Fibonacci Number: A sequence of numbers in which each number is the sum of the two preceding ones.
