## **Lesson Plan: Practical Applications of Functions in Python (with Solutions)**

---

### **1. Exercises for Functions**

#### **Exercise 1: Multiplication Function**
**Task:**  
Write a function that takes two numbers as arguments and returns their product.

**Solution:**
```python
def multiply_numbers(a, b):
    return a * b

# Test the function
result = multiply_numbers(4, 5)
print("Product:", result)
```

---

#### **Exercise 2: Area of a Rectangle**
**Task:**  
Create a function to calculate and return the area of a rectangle given its length and width.

**Solution:**
```python
def rectangle_area(length, width):
    return length * width

# Test the function
area = rectangle_area(10, 5)
print("Area of rectangle:", area)
```

---

#### **Exercise 3: Recursive Fibonacci**
**Task:**  
Implement a recursive function to calculate the nth Fibonacci number.

**Solution:**
```python
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Test the function
n = 10
print(f"The {n}th Fibonacci number is:", fibonacci(n))
```

---

### **2. Real-World Applications**

#### **Application 1: Simple Calculator**
**Task:**  
Write a function-based calculator that supports addition, subtraction, multiplication, and division.

**Solution:**
```python
def calculator(a, b, operation):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        return a / b
    else:
        return "Invalid operation"

# Test the function
print("Addition:", calculator(8, 4, "add"))
print("Division:", calculator(8, 4, "divide"))
```

---

#### **Application 2: Splitting Full Names**
**Task:**  
Create a function to split a full name into first and last names.

**Solution:**
```python
def split_name(full_name):
    first_name, last_name = full_name.split()
    return first_name, last_name

# Test the function
first, last = split_name("Alice Johnson")
print("First Name:", first)
print("Last Name:", last)
```

---

#### **Application 3: Checking Prime Numbers**
**Task:**  
Write a function to check if a given number is a prime number.

**Solution:**
```python
def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Test the function
print("Is 7 prime?", is_prime(7))
print("Is 10 prime?", is_prime(10))
```

---

### **3. Challenges**

#### **Challenge 1: Palindrome Checker**
**Task:**  
Write a function that checks if a given string is a palindrome.

**Solution:**
```python
def is_palindrome(string):
    return string == string[::-1]

# Test the function
print("Is 'radar' a palindrome?", is_palindrome("radar"))
print("Is 'hello' a palindrome?", is_palindrome("hello"))
```

---

#### **Challenge 2: Temperature Conversion**
**Task:**  
Write functions to convert temperatures between Celsius and Fahrenheit.

**Solution:**
```python
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Test the functions
print("25°C to Fahrenheit:", celsius_to_fahrenheit(25))
print("77°F to Celsius:", fahrenheit_to_celsius(77))
```

---

#### **Challenge 3: Student Grade Calculator**
**Task:**  
Write a function that calculates the average of a list of grades and returns the letter grade.

**Solution:**
```python
def calculate_grade(grades):
    average = sum(grades) / len(grades)
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"

# Test the function
grades = [85, 90, 78, 92]
print("Letter Grade:", calculate_grade(grades))
```

---

#### **Challenge 4: Factorial with Loop**
**Task:**  
Write a function to calculate the factorial of a number using a loop instead of recursion.

**Solution:**
```python
def factorial_loop(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

# Test the function
print("Factorial of 5:", factorial_loop(5))
```

---
