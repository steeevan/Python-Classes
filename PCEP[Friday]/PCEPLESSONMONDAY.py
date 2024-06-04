### Lesson Plan: Introduction to Loops and Functions in Python

---

Objective:
Students will understand and be able to use loops and functions in Python. They will learn to identify key parts of a function and determine the output of code involving loops and conditional statements.

Materials:
- Computers with Python installed
- Projector/Whiteboard
- Handouts of code examples and exercises

Duration:
1 hour

---

### Part 1: Introduction to Loops

1.1 What are Loops?
- Definition: A loop in programming is a control structure that allows you to repeat a block of code multiple times based on a condition. Loops can significantly reduce the redundancy of code and help in performing repetitive tasks efficiently.
- Types of Loops in Python:
  - `for` loop: Iterates over a sequence (like a list, tuple, or range) and executes the code block for each item.
  - `while` loop: Repeats the code block as long as the given condition is `True`.

1.2 `for` Loop
- Syntax:
  ```python
  for variable in iterable:
      # code block
  ```
- Example:
  ```python
  for i in range(5):
      print(i)
  ```
  - Explanation: This loop will print numbers from 0 to 4. `range(5)` generates a sequence of numbers from 0 to 4.

1.3 `while` Loop
- Syntax:
  ```python
  while condition:
      # code block
  ```
- Example:
  ```python
  count = 0
  while count < 5:
      print(count)
      count += 1
  ```
  - Explanation: This loop will also print numbers from 0 to 4. The loop continues to run as long as `count` is less than 5.

1.4 Conditional Statements within Loops
- Example:
  ```python
  for i in range(10):
      if i % 2 == 0:
          print(i, "is even")
      else:
          print(i, "is odd")
  ```
  - Explanation: This loop prints whether each number from 0 to 9 is even or odd by using an `if` statement to check if the number is divisible by 2.

Activity 1: Determine the Output
- Code Example 1:
  ```python
  for i in range(3):
      for j in range(2):
          print(i, j)
  ```
  - Question: What is the output of the above code?
  - Expected Answer: 
    ```
    0 0
    0 1
    1 0
    1 1
    2 0
    2 1
    ```

Code Example 2:
  ```python
  count = 0
  while count < 4:
      if count % 2 == 0:
          print(count, "is even")
      else:
          print(count, "is odd")
      count += 1
  ```
  - Question: What is the output of the above code?
  - Expected Answer:
    ```
    0 is even
    1 is odd
    2 is even
    3 is odd
    ```

---

### Part 2: Introduction to Functions

2.1 What is a Function?
- Definition: A function is a reusable block of code that performs a specific task. Functions help in making the code modular, organized, and easier to manage. Functions can take inputs, called parameters, and can return an output.
- Syntax:
  ```python
  def function_name(parameters):
      # code block
  ```

2.2 Defining and Calling Functions
- Example:
  ```python
  def greet(name):
      print("Hello, " + name + "!")
  
  greet("Alice")
  ```
  - Explanation: The function `greet` takes a parameter `name` and prints a greeting message. When calling `greet("Alice")`, it prints "Hello, Alice!".

2.3 Key Parts of a Function
- Function Name: The name of the function (e.g., `greet`).
- Parameters: Variables that the function can accept (e.g., `name`).
- Function Body: The code block that runs when the function is called.
- Return Statement (Optional): Specifies the value that the function returns.

2.4 Purpose of Functions
- Reusability: Functions allow you to reuse code without rewriting it.
- Modularity: Functions help in organizing code into logical blocks.
- Abstraction: Functions can hide complex logic, making code easier to understand.

Activity 2: Identify Key Parts and Purpose
- Code Example:
  ```python
  def add_numbers(a, b):
      return a + b
  
  result = add_numbers(3, 4)
  print(result)
  ```
  - Questions:
    1. Identify the function name.
    2. Identify the parameters.
    3. What does the function do?
    4. What is the purpose of this function?
  - Expected Answers:
    1. `add_numbers`
    2. `a`, `b`
    3. Adds two numbers and returns the result.
    4. The purpose is to add two numbers and return their sum.

Code Example 2:
  ```python
  def is_even(number):
      if number % 2 == 0:
          return True
      else:
          return False
  
  print(is_even(7))
  ```
  - Questions:
    1. Identify the function name.
    2. Identify the parameters.
    3. What does the function do?
    4. What is the purpose of this function?
  - Expected Answers:
    1. `is_even`
    2. `number`
    3. Checks if a number is even and returns `True` or `False`.
    4. The purpose is to determine if a given number is even.

---

### Coding Challenges: Loops and Functions in Python

---

Objective:
Students will apply their knowledge of loops and functions by writing Python code to solve various problems.

Duration:
45 minutes

---

### Challenge 1: Count Vowels

Problem:
Write a function `count_vowels` that takes a string as input and returns the number of vowels (a, e, i, o, u) in the string.

Requirements:
- Use a `for` loop to iterate through the string.
- Use an `if` statement to check if a character is a vowel.

Function Signature:
```python
def count_vowels(input_string):
    # Your code here
```

Example:
```python
print(count_vowels("hello world"))  # Output: 3
```

---

### Challenge 2: Reverse a List

Problem:
Write a function `reverse_list` that takes a list as input and returns a new list with the elements in reverse order.

Requirements:
- Use a `for` loop to iterate through the list.
- Use an accumulator to build the reversed list.

Function Signature:
```python
def reverse_list(input_list):
    # Your code here
```

Example:
```python
print(reverse_list([1, 2, 3, 4, 5]))  # Output: [5, 4, 3, 2, 1]
```

---

### Challenge 3: Sum of Digits

Problem:
Write a function `sum_of_digits` that takes an integer and returns the sum of its digits.

Requirements:
- Use a `while` loop to extract digits from the number.
- Use an accumulator to sum the digits.

Function Signature:
```python
def sum_of_digits(n):
    # Your code here
```

Example:
```python
print(sum_of_digits(1234))  # Output: 10
```

---

### Challenge 4: Find the Maximum Value

Problem:
Write a function `find_max` that takes a list of numbers and returns the maximum value in the list.

Requirements:
- Use a `for` loop to iterate through the list.
- Use a variable to keep track of the maximum value.

Function Signature:
```python
def find_max(numbers):
    # Your code here
```

Example:
```python
print(find_max([3, 5, 7, 2, 8]))  # Output: 8
```

---

### Challenge 5: Palindrome Checker

Problem:
Write a function `is_palindrome` that takes a string and returns `True` if the string is a palindrome (reads the same forwards and backwards) and `False` otherwise.

Requirements:
- Use a `for` loop to compare characters from the start and end of the string.
- Use an `if` statement to check for mismatches.

Function Signature:
```python
def is_palindrome(s):
    # Your code here
```

Example:
```python
print(is_palindrome("radar"))  # Output: True
print(is_palindrome("hello"))  # Output: False
```

---

Conclusion:
- Review and discuss solutions for each challenge.
- Encourage students to ask questions and explain their thought processes.

---

