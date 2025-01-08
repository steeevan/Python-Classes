

## 1. Lists and Tuples

### Overview
- **Lists**  
  - Mutable (elements can be changed, added, or removed)  
  - Ordered collection (elements maintain a defined sequence)  
  - Common operations: indexing, slicing, `append()`, `insert()`, `remove()`, `sort()`, `reverse()`

- **Tuples**  
  - Immutable (elements cannot be changed after creation)  
  - Ordered collection  
  - Useful for data that should not be modified

### Key Points
- Creation and initialization:
  ```python
  my_list = [1, 2, 3]
  my_tuple = (1, 2, 3)
  ```
- Indexing and slicing (both lists and tuples):
  ```python
  my_list[0]  # Access first element
  my_tuple[-1]  # Access last element
  my_list[1:3]  # Slice elements from index 1 to 2
  ```
- Manipulation (lists only):
  ```python
  my_list.append(4)
  my_list.insert(1, 'inserted')
  my_list.remove(2)
  ```

### Practice Exercises
1. Create a list of your favorite foods and perform various operations (append, remove, slice).
2. Convert the list of foods into a tuple and observe what happens if you try to change an element.
3. Write a program to reverse a list without using any built-in reverse methods.

---

## 2. Working with Strings

### Overview
- Strings are **immutable** sequences of characters.
- Common operations: indexing, slicing, concatenation, and various string methods (`upper()`, `lower()`, `split()`, `replace()`, `find()`, etc.).
- **String formatting** allows for more readable code and controlling the output format:
  - `f-strings` (formatted string literals)
  - `format()` method
  - `%` formatting (older style)

### Key Points
- Basic operations:
  ```python
  text = "Hello World"
  text[0]        # 'H'
  text[1:5]      # 'ello'
  text.upper()   # 'HELLO WORLD'
  text.split()   # ['Hello', 'World']
  ```
- String concatenation and repetition:
  ```python
  "Hello" + " " + "World"  # "Hello World"
  "Hello" * 3              # "HelloHelloHello"
  ```
- Formatting:
  ```python
  name = "Alice"
  age = 25
  # f-string
  print(f"My name is {name}, and I am {age} years old.")
  
  # format() method
  print("My name is {}, and I am {} years old.".format(name, age))

  # % formatting (older style)
  print("My name is %s, and I am %d years old." % (name, age))
  ```

### Practice Exercises
1. Write a function that takes a string and returns it in reverse (e.g., `"Hello" -> "olleH"`).
2. Experiment with different string methods: try trimming whitespace, splitting by different delimiters, and replacing certain characters.
3. Practice string formatting by creating a sentence with placeholders for name, age, and hobby, then format it using all three methods mentioned above.

---

## 3. Loops (for and while)

### Overview
- **For loops**: iterate over a sequence of items (e.g., list, tuple, string).
- **While loops**: run as long as a condition remains true.

### Key Points
- `for` loop:
  ```python
  numbers = [1, 2, 3]
  for num in numbers:
      print(num)
  ```
- `while` loop:
  ```python
  counter = 0
  while counter < 5:
      print(counter)
      counter += 1
  ```
- Loop control statements:
  - `break`: exit the current loop entirely
  - `continue`: skip the current iteration of the loop and move to the next
  - `pass`: do nothing (placeholder statement)

### Practice Exercises
1. Use a `for` loop to iterate through a list of integers and find their sum.
2. Write a `while` loop that prompts the user for input until they type “quit.”
3. Experiment with `break` and `continue` in a loop to understand their effects.

---

## 4. Dictionaries and Sets

### Overview
- **Dictionaries**  
  - Key-value pairs  
  - Mutable, but keys must be immutable types (e.g., strings, numbers, tuples if they do not contain mutable elements)  
  - Used for fast lookups and data retrieval

- **Sets**  
  - Unordered collection of unique elements (no duplicates)  
  - Mutable (elements can be added or removed)  
  - Very efficient for membership testing (checking if something is in the set)

### Key Points
- Dictionary creation and access:
  ```python
  my_dict = {"apple": 3, "banana": 2}
  my_dict["apple"]           # 3
  my_dict["orange"] = 5      # Adding a new key-value pair
  ```
- Dictionary methods:  
  - `items()`, `keys()`, `values()`, `get()`, `pop()`
- Set creation and operations:
  ```python
  my_set = {1, 2, 3}
  my_set.add(4)
  my_set.remove(2)
  ```
- Set operations:  
  - Union (`|`), intersection (`&`), difference (`-`)

### Practice Exercises
1. Create a dictionary of students and their grades. Add, remove, and modify entries.
2. Write a program that checks if a given key exists in the dictionary before adding or updating a value.
3. Use sets to find common elements and unique elements in two different lists.
4. Practice with set methods (union, intersection, difference) on sample sets.

Below you’ll find a set of **practice problems** related to each of the topics—Lists & Tuples, Working with Strings, Loops, and Dictionaries & Sets—**with full solutions**. These are designed to help students strengthen their understanding and coding skills.

---

## 1. Lists and Tuples

### Problem 1: Rotate a List
**Task**  
Write a function `rotate_list(lst, n)` that takes a list `lst` and an integer `n`. The function should return a **new list** with the elements rotated **to the right** by `n` positions. For example:
- If `lst = [1, 2, 3, 4, 5]` and `n = 2`, the result should be `[4, 5, 1, 2, 3]`.

**Solution**
```python
def rotate_list(lst, n):
    # If n is larger than the length of the list, reduce it modulo len(lst)
    n = n % len(lst)
    # Slice the list at the rotation point
    return lst[-n:] + lst[:-n]

# Testing the function
test_list = [1, 2, 3, 4, 5]
rotated = rotate_list(test_list, 2)
print(rotated)  # Output: [4, 5, 1, 2, 3]
```

### Problem 2: Convert Between List and Tuple
**Task**  
1. Given a list of numbers, convert it to a tuple.  
2. Try to change one of the elements in the tuple.  
3. Print the results to observe what happens.

**Solution**
```python
# Step 1: Convert list to tuple
numbers_list = [10, 20, 30, 40]
numbers_tuple = tuple(numbers_list)
print("Tuple:", numbers_tuple)  # Output: (10, 20, 30, 40)

# Step 2: Try changing an element in the tuple (this will cause an error)
try:
    numbers_tuple[0] = 99
except TypeError as e:
    print("Error:", e)  # Tuples are immutable
```

### Problem 3: Reverse a List Without Built-In Methods
**Task**  
Write a function to reverse a list **in place** without using the built-in `reverse()` method or slicing tricks. For instance, `[1, 2, 3, 4]` should become `[4, 3, 2, 1]`.

**Solution**
```python
def reverse_list(lst):
    left = 0
    right = len(lst) - 1
    while left < right:
        # Swap elements
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1

my_list = [1, 2, 3, 4]
reverse_list(my_list)
print(my_list)  # Output: [4, 3, 2, 1]
```

---

## 2. Working with Strings

### Problem 1: Palindrome Checker
**Task**  
Write a function `is_palindrome(text)` that checks if a given string is a palindrome (reads the same forward and backward). Ignore **case** and **spaces**.  
- Example: `"A nut for a jar of tuna"` should return `True`.

**Solution**
```python
def is_palindrome(text):
    # Remove spaces and make lowercase
    filtered = text.replace(" ", "").lower()
    # Check if filtered string is the same backwards
    return filtered == filtered[::-1]

test_cases = ["A nut for a jar of tuna", "Hello", "Racecar", "Was it a cat I saw"]
for t in test_cases:
    print(t, "->", is_palindrome(t))
# A nut for a jar of tuna -> True
# Hello -> False
# Racecar -> True
# Was it a cat I saw -> True
```

### Problem 2: Character Frequency in a String
**Task**  
Write a program that takes a string and prints the **frequency** of each character in the string (excluding spaces).  
- For example, `"Hello World"` should display:
  - `H: 1, e: 1, l: 3, o: 2, W: 1, r: 1, d: 1`

**Solution**
```python
def char_frequency(text):
    freq = {}
    for char in text:
        if char == " ":
            continue  # skip spaces
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    return freq

input_str = "Hello World"
result = char_frequency(input_str)
for char, count in result.items():
    print(f"{char}: {count}")
# Example output:
# H: 1
# e: 1
# l: 3
# o: 2
# W: 1
# r: 1
# d: 1
```

### Problem 3: Custom String Formatting
**Task**  
Write a function `format_greeting(name, age, hobby)` that returns a formatted string using **f-strings**, `format()`, and **% formatting**. Compare the outputs.

**Solution**
```python
def format_greeting(name, age, hobby):
    f_string = f"My name is {name}. I'm {age} years old and I love {hobby}."
    format_method = "My name is {}. I'm {} years old and I love {}.".format(name, age, hobby)
    percent_format = "My name is %s. I'm %d years old and I love %s." % (name, age, hobby)
    return f_string, format_method, percent_format

greetings = format_greeting("Alice", 25, "painting")
print("F-String:       ", greetings[0])
print("Format Method:  ", greetings[1])
print("Percent Format: ", greetings[2])
```

---

## 3. Loops (for and while)

### Problem 1: Summation of a List
**Task**  
Use a `for` loop to calculate the sum of all numbers in a list. Then, use a `while` loop to do the same calculation.

**Solution**
```python
numbers = [5, 7, 2, 10, 3]

# For loop
total_for = 0
for num in numbers:
    total_for += num
print("Sum using for loop:", total_for)

# While loop
index = 0
total_while = 0
while index < len(numbers):
    total_while += numbers[index]
    index += 1
print("Sum using while loop:", total_while)
```

### Problem 2: User Input with While Loop
**Task**  
Write a program that repeatedly asks the user to input a word until they type **“quit”**. Collect all non-quit words in a list and print the list at the end.

> **Note**: Depending on the environment (online IDE, Jupyter, etc.), you might adapt user input logic or just simulate the process.

**Solution**  
*(Below is a code snippet that assumes you can run it in an interactive environment.)*
```python
def collect_words():
    collected = []
    while True:
        user_input = input("Enter a word (type 'quit' to stop): ")
        if user_input.lower() == "quit":
            break
        collected.append(user_input)
    return collected

words_list = collect_words()
print("Collected words:", words_list)
```

### Problem 3: FizzBuzz Variation
**Task**  
Use a `for` loop to print the numbers from **1 to 20**. For multiples of 3, print **"Fizz"**, for multiples of 5, print **"Buzz"**, and for multiples of both 3 and 5, print **"FizzBuzz"**.

**Solution**
```python
for i in range(1, 21):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
```

---

## 4. Dictionaries and Sets

### Problem 1: Dictionary of Grades
**Task**  
Create a dictionary of **student names** and their **grades**. Implement functions to:
1. Add a new student with a grade (if the student doesn’t exist).  
2. Update the grade of an existing student.  
3. Remove a student (if they exist).  
4. Print all students and their grades.

**Solution**
```python
def add_student(grades_dict, name, grade):
    if name in grades_dict:
        print(f"{name} already exists with grade {grades_dict[name]}.")
    else:
        grades_dict[name] = grade
        print(f"Added {name} with grade {grade}.")

def update_grade(grades_dict, name, grade):
    if name in grades_dict:
        grades_dict[name] = grade
        print(f"Updated {name} to grade {grade}.")
    else:
        print(f"{name} does not exist in the records.")

def remove_student(grades_dict, name):
    if name in grades_dict:
        del grades_dict[name]
        print(f"Removed {name}.")
    else:
        print(f"{name} not found in the records.")

def print_grades(grades_dict):
    for name, grade in grades_dict.items():
        print(f"{name}: {grade}")

# Example usage
grades = {}
add_student(grades, "Alice", 90)
add_student(grades, "Bob", 85)
add_student(grades, "Alice", 95)  # Already exists
update_grade(grades, "Bob", 88)
remove_student(grades, "Charlie")  # Does not exist
print_grades(grades)
```

### Problem 2: Check Existence Before Adding
**Task**  
Write a function that takes a dictionary and a **key-value** pair. If the **key** already exists, **ignore** the addition. Otherwise, **add** it to the dictionary. Return whether the addition happened or not.

**Solution**
```python
def safe_add(dictionary, key, value):
    if key in dictionary:
        return False
    dictionary[key] = value
    return True

my_dict = {"apple": 3, "banana": 2}
if safe_add(my_dict, "apple", 10):
    print("Added 'apple' -> 10.")
else:
    print("'apple' key already exists, no addition made.")

print(my_dict)
# Output:
# 'apple' key already exists, no addition made.
# {'apple': 3, 'banana': 2}
```

### Problem 3: Set Operations
**Task**  
Create two sets of integers:
1. Print their **union**.  
2. Print their **intersection**.  
3. Print their **difference** (set1 - set2 and set2 - set1).  
4. Check if one set is a **subset** of the other.

**Solution**
```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# 1. Union
union_set = set1 | set2
print("Union:", union_set)  # {1, 2, 3, 4, 5, 6}

# 2. Intersection
intersection_set = set1 & set2
print("Intersection:", intersection_set)  # {3, 4}

# 3. Difference
diff1 = set1 - set2
diff2 = set2 - set1
print("set1 - set2:", diff1)  # {1, 2}
print("set2 - set1:", diff2)  # {5, 6}

# 4. Subset check
print("Is set1 a subset of set2?", set1.issubset(set2))  # False
print("Is {3, 4} a subset of set1?", {3, 4}.issubset(set1))  # True
```

---

