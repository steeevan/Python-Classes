## **Lesson Plan: Practical Applications of Loops (with Solutions)**

---

### **1. Exercises for "for" and "while" Loops**

#### **Exercise 1: Multiplication Table**
**Task:**  
Write a program that prints the multiplication table for a given number (e.g., 7).

**Solution:**
```python
number = 7
print(f"Multiplication Table for {number}:")

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
```

---

#### **Exercise 2: Factorial Calculation**
**Task:**  
Create a program that calculates and prints the factorial of a given number.

**Solution:**
```python
number = 5
factorial = 1

for i in range(1, number + 1):
    factorial *= i

print(f"Factorial of {number} is {factorial}")
```

---

#### **Exercise 3: Guessing Game**
**Task:**  
Implement a guessing game where the user guesses a secret number until they get it right.

**Solution:**
```python
import random

secret_number = random.randint(1, 10)
guess = 0

print("Guess the secret number between 1 and 10!")

while guess != secret_number:
    guess = int(input("Enter your guess: "))
    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print("Correct! You guessed the secret number.")
```

---

### **2. Real-World Applications**

#### **Application 1: Summing Numbers**
**Task:**  
Write a program to calculate the sum of all numbers from 1 to a user-defined number.

**Solution:**
```python
n = 10
total = 0

for i in range(1, n + 1):
    total += i

print(f"The sum of numbers from 1 to {n} is {total}")
```

---

#### **Application 2: Finding Prime Numbers**
**Task:**  
Create a program to find all prime numbers in a given range (e.g., 1 to 50).

**Solution:**
```python
n = 50
prime_numbers = []

for num in range(2, n + 1):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        prime_numbers.append(num)

print(f"Prime numbers between 2 and {n}: {prime_numbers}")
```

---

#### **Application 3: Countdown Timer**
**Task:**  
Create a countdown timer starting from 10 and print "Liftoff!" at the end.

**Solution:**
```python
countdown = 10

while countdown > 0:
    print(f"Countdown: {countdown}")
    countdown -= 1

print("Liftoff!")
```

---

#### **Application 4: Even and Odd Number Separator**
**Task:**  
Write a program to separate a list of numbers into two lists: one for even numbers and one for odd numbers.

**Solution:**
```python
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = []
odd_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

print("Even Numbers:", even_numbers)
print("Odd Numbers:", odd_numbers)
```

---

### **3. Challenges**

#### **Challenge 1: Find the Maximum**
**Task:**  
Write a program to find the maximum number in a list using a loop.

**Solution:**
```python
numbers = [5, 3, 8, 6, 2, 7, 4, 1]
max_number = numbers[0]

for number in numbers:
    if number > max_number:
        max_number = number

print(f"The maximum number is {max_number}")
```

---

#### **Challenge 2: Reverse a String**
**Task:**  
Write a program that reverses a string using a loop.

**Solution:**
```python
text = "Python"
reversed_text = ""

for char in text:
    reversed_text = char + reversed_text

print(f"The reversed string is '{reversed_text}'")
```

---

#### **Challenge 3: Fibonacci Sequence**
**Task:**  
Generate the Fibonacci sequence up to the 10th term using a loop.

**Solution:**
```python
n_terms = 10
a, b = 0, 1

print("Fibonacci Sequence:")
for _ in range(n_terms):
    print(a, end=" ")
    a, b = b, a + b
```

---

#### **Challenge 4: Pattern Printing**
**Task:**  
Print the following pattern for a given number of rows:  
```
*
**
***
****
*****
```

**Solution:**
```python
rows = 5

for i in range(1, rows + 1):
    print("*" * i)
```

---
