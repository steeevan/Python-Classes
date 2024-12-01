### **Python Lesson: Anonymous Functions (Lambda Functions)**

---

#### **Lesson Objectives**
By the end of this lesson, students will:
1. Understand what anonymous functions are and why they are used.
2. Learn the syntax and use cases of lambda functions in Python.
3. Explore the differences between lambda functions and regular functions.
4. Practice writing and applying lambda functions in real-world scenarios.

---

### **Lesson Outline**

#### **1. Introduction to Anonymous Functions**
- **Definition**: Anonymous functions are functions without a name, often used for short-term tasks. In Python, these are implemented using the `lambda` keyword.
- **Purpose**: To create simple functions inline without using the `def` keyword.
- **Syntax**:
  ```python
  lambda arguments: expression
  ```

#### **2. Key Characteristics**
- A lambda function can have any number of arguments, but only one expression.
- The result of the expression is automatically returned.
- They are commonly used as arguments for higher-order functions like `map()`, `filter()`, and `reduce()`.

---

#### **3. Examples**

1. **Basic Lambda Function**
   ```python
   # A simple lambda function to add 10 to a number
   add_ten = lambda x: x + 10
   print(add_ten(5))  # Output: 15
   ```

2. **Lambda with Multiple Arguments**
   ```python
   # A lambda function to calculate the product of two numbers
   multiply = lambda x, y: x * y
   print(multiply(3, 4))  # Output: 12
   ```

3. **Using Lambda with `map()`**
   ```python
   # Doubling each element in a list
   numbers = [1, 2, 3, 4, 5]
   doubled = list(map(lambda x: x * 2, numbers))
   print(doubled)  # Output: [2, 4, 6, 8, 10]
   ```

4. **Using Lambda with `filter()`**
   ```python
   # Filtering even numbers from a list
   numbers = [1, 2, 3, 4, 5, 6]
   evens = list(filter(lambda x: x % 2 == 0, numbers))
   print(evens)  # Output: [2, 4, 6]
   ```

5. **Using Lambda with `reduce()`**
   ```python
   from functools import reduce
   # Finding the product of all elements in a list
   numbers = [1, 2, 3, 4]
   product = reduce(lambda x, y: x * y, numbers)
   print(product)  # Output: 24
   ```

---

#### **4. Guidelines for Using Lambda Functions**
1. Use them for short and simple operations.
2. Avoid using them for complex logic—use `def` instead.
3. Understand that they are less readable than named functions in larger codebases.
4. Use them in conjunction with built-in Python functions like `map`, `filter`, and `sorted`.

---

### **Class Activities**

#### **Activity 1: Write a Lambda Function**
- **Task**: Write a lambda function that:
  1. Takes a single number and returns its square.
  2. Takes two numbers and returns the larger number.
- **Expected Output**:
  ```python
  square = lambda x: x ** 2
  print(square(4))  # Output: 16

  larger = lambda x, y: x if x > y else y
  print(larger(3, 7))  # Output: 7
  ```

---

#### **Activity 2: Filter Specific Items**
- **Task**: Given a list of strings, filter out all strings with less than 5 characters using a lambda function.
- **Hint**: Use the `filter()` function.
- **Example Input**:
  ```python
  words = ["apple", "cat", "banana", "dog", "

```python
  words = ["apple", "cat", "banana", "dog", "elephant"]
  long_words = list(filter(lambda word: len(word) >= 5, words))
  print(long_words)  # Output: ['apple', 'banana', 'elephant']
  ```

---

#### **Activity 3: Sort Using Lambda**
- **Task**: Sort a list of tuples based on the second element in each tuple.
- **Example Input**:
  ```python
  pairs = [(1, 3), (4, 1), (2, 2), (3, 4)]
  sorted_pairs = sorted(pairs, key=lambda x: x[1])
  print(sorted_pairs)  # Output: [(4, 1), (2, 2), (1, 3), (3, 4)]
  ```

---

#### **Activity 4: Map Function with Lambda**
- **Task**: Use `map()` to convert a list of temperatures in Celsius to Fahrenheit.
- **Formula**: `F = C * 9/5 + 32`
- **Example Input**:
  ```python
  celsius = [0, 20, 37, 100]
  fahrenheit = list(map(lambda c: c * 9/5 + 32, celsius))
  print(fahrenheit)  # Output: [32.0, 68.0, 98.6, 212.0]
  ```

---

### **Reflection and Discussion**
1. When is it better to use a lambda function instead of a named function?
2. Discuss readability issues when overusing lambda functions.
3. How do lambda functions enhance the functionality of Python’s built-in tools like `map`, `filter`, and `sorted`?

---

### **Homework**
1. **Practice Problem**: Create a lambda function to:
   - Count vowels in a given string.
   - Reverse the characters of a string.
2. **Challenge**: Write a program that uses lambda functions to find:
   - The longest word in a list.
   - The sum of squares of a list of numbers using `reduce()`.

---
