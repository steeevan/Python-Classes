# ===============================================
# Lesson Plan: Loops (for and while) in Python
# ===============================================

# **Objective:** Teach the use of for and while loops for repetitive tasks and iterations in Python.

# ===============================================
# 1. Introduction to Loops
# ===============================================

# Loops are control structures that allow you to repeat a block of code multiple times. They are essential for automating repetitive tasks and iterating over collections of data.

# ===============================================
# 2. The "for" Loop
# ===============================================

# The "for" loop is used to iterate over a sequence (such as a list, tuple, string, or range) and execute a block of code for each element in the sequence.

# Example:
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(fruit)

# ===============================================
# 3. The "while" Loop
# ===============================================

# The "while" loop is used to repeatedly execute a block of code as long as a specified condition is True.

# Example:
count = 1

while count <= 5:
    print("Count:", count)
    count += 1

# ===============================================
# 4. Loop Control Statements
# ===============================================

# Loop control statements allow you to control the flow of loops.

# - "break": Terminates the loop prematurely.
# - "continue": Skips the current iteration and continues to the next one.

# Example:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in numbers:
    if number % 2 == 0:
        print("Even:", number)
    else:
        continue

# ===============================================
# 5. Looping with Range
# ===============================================

# The "range()" function generates a sequence of numbers, which can be used with "for" loops to specify a range of iterations.

# Example:
for i in range(1, 6):
    print(i)

# ===============================================
# 6. Additional Examples
# ===============================================

# Example 1: Sum of Numbers
total = 0

for num in range(1, 6):
    total += num

print("Sum of numbers:", total)

# Example 2: Finding Prime Numbers
prime_numbers = []

for num in range(2, 20):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        prime_numbers.append(num)

print("Prime numbers:", prime_numbers)

# Example 3: Countdown
countdown = 5

while countdown > 0:
    print("Countdown:", countdown)
    countdown -= 1

# ===============================================
# 7. Exercises
# ===============================================

# Exercise 1: Write a program that prints the multiplication table of a given number (e.g., 7 times table).
# Exercise 2: Create a program that calculates and prints the factorial of a given number.
# Exercise 3: Implement a guessing game where the user has to guess a secret number. Use a "while" loop until the correct number is guessed.

# ===============================================
# 8. Conclusion
# ===============================================

# In this lesson, you've learned about "for" and "while" loops in Python, which are used for repetitive tasks and iterations. Loops are powerful tools for automating tasks and processing data efficiently.

# Continue practicing with loops to become proficient in using them for various programming challenges.

# ===============================================
# Vocabulary Words and Definitions
# ===============================================

# - Loop: A control structure that allows you to repeat a block of code multiple times.
# - Iteration: Each execution of the loop's code block is called an iteration.
# - Sequence: An ordered collection of elements, such as a list, tuple, string, or range.
# - Loop Control Statements: Statements like "break" and "continue" that control the flow of loops.
# - Range: A function that generates a sequence of numbers for use in loops.
