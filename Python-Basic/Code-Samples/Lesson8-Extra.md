
---

## **Lesson Plan: Practical Applications of Dictionaries and Sets**

---

### **1. Exercises for Dictionaries**

#### **Exercise 1: Creating and Accessing a Dictionary**
- Create a dictionary to store information about a movie:
  - Keys: `title`, `director`, `year`, `rating`
  - Values: Assign any movie details of your choice.
- Access and print:
  - The title of the movie.
  - The year of release.

#### **Exercise 2: Modifying a Dictionary**
- Add a new key-value pair to the movie dictionary: `genre`.
- Update the `rating` key to a new value.

#### **Exercise 3: Word Frequency Counter**
- Write a program to count the frequency of each word in the sentence:
  - "Dictionaries are useful in Python programming."
- Store the results in a dictionary.

#### **Challenge: Dictionary for Data Analysis**
- You are given a list of employee records as tuples:  
  `[("Alice", "HR"), ("Bob", "Engineering"), ("Alice", "HR"), ("Charlie", "Marketing")]`
  - Create a dictionary to count the number of employees in each department.

---

### **2. Exercises for Sets**

#### **Exercise 1: Deduplicating a List**
- Given a list of student names with duplicates:  
  `["Alice", "Bob", "Alice", "Charlie", "Bob", "Alice"]`
  - Use a set to create a list of unique student names.

#### **Exercise 2: Set Operations**
- Given two sets of integers:
  - `set1 = {1, 2, 3, 4}`
  - `set2 = {3, 4, 5, 6}`
  - Find:
    - The union of both sets.
    - The intersection of both sets.
    - The difference of `set1` from `set2`.

#### **Challenge: Set for Membership Testing**
- Write a program to check whether a given number is part of a predefined set of even numbers. The set should contain the numbers `{2, 4, 6, 8, 10}`.

---

### **3. Real-World Applications**

#### **Application 1: Student Grades Management**
- Create a dictionary where:
  - Keys: Student names.
  - Values: Lists of their grades (e.g., `{"Alice": [90, 85, 88]}`).
- Write a program to calculate the average grade for each student.

#### **Application 2: Inventory Tracker**
- Create a dictionary to manage an inventory:
  - Keys: Product names (e.g., `apples`, `oranges`).
  - Values: Quantities of each product.
- Implement functionality to:
  - Add new products to the inventory.
  - Update the quantity of an existing product.
  - Check if a product is in stock.

#### **Application 3: Keyword Deduplication**
- Given a list of keywords for a website, remove duplicates using a set:
  `["python", "coding", "python", "tutorial", "coding"]`

---

### **4. Challenges to Solve Independently**

#### **Challenge 1: Social Media Analytics**
- Given a list of hashtags from social media posts:
  `["#python", "#AI", "#machinelearning", "#AI", "#coding", "#python"]`
  - Use a dictionary to count the occurrences of each hashtag.
  - Use a set to find the unique hashtags.

#### **Challenge 2: Library System**
- Create a library system where:
  - A dictionary stores book titles as keys and their availability (`True` or `False`) as values.
  - Write a program that:
    - Adds new books to the library.
    - Checks if a book is available.
    - Updates the availability when a book is borrowed or returned.

#### **Challenge 3: Student Enrollments**
- Given the enrollments of two different classes:
  - `class1 = {"Alice", "Bob", "Charlie"}`
  - `class2 = {"Bob", "David", "Eve"}`
  - Find:
    - Students enrolled in both classes.
    - Students enrolled in only one class.
    - All unique students across both classes.

#### **Challenge 4: Real Estate Listings**
- Write a program that:
  - Takes a list of real estate listings, with duplicate listings (e.g., addresses).
  - Uses a set to remove duplicates and store only unique addresses.
  - Prints the total number of unique listings.

---
### Instructors Guide
---

## **Lesson Plan: Practical Applications of Dictionaries and Sets (with Solutions)**

---

### **1. Exercises for Dictionaries**

#### **Exercise 1: Creating and Accessing a Dictionary**
**Task:**  
Create a dictionary for a movie and access its title and year.

**Solution:**
```python
movie = {
    "title": "Inception",
    "director": "Christopher Nolan",
    "year": 2010,
    "rating": 8.8
}

# Access values
print("Title:", movie["title"])
print("Year:", movie["year"])
```

#### **Exercise 2: Modifying a Dictionary**
**Task:**  
Add a genre and update the rating.

**Solution:**
```python
movie["genre"] = "Science Fiction"
movie["rating"] = 9.0

print("Updated Movie:", movie)
```

#### **Exercise 3: Word Frequency Counter**
**Task:**  
Count the frequency of words in a sentence.

**Solution:**
```python
sentence = "Dictionaries are useful in Python programming"
word_count = {}

for word in sentence.split():
    word = word.lower()
    word_count[word] = word_count.get(word, 0) + 1

print("Word Frequency:", word_count)
```

#### **Challenge: Dictionary for Data Analysis**
**Task:**  
Count employees in each department.

**Solution:**
```python
records = [("Alice", "HR"), ("Bob", "Engineering"), ("Alice", "HR"), ("Charlie", "Marketing")]
department_count = {}

for _, dept in records:
    department_count[dept] = department_count.get(dept, 0) + 1

print("Department Count:", department_count)
```

---

### **2. Exercises for Sets**

#### **Exercise 1: Deduplicating a List**
**Task:**  
Remove duplicates from a list of student names.

**Solution:**
```python
students = ["Alice", "Bob", "Alice", "Charlie", "Bob", "Alice"]
unique_students = set(students)

print("Unique Students:", unique_students)
```

#### **Exercise 2: Set Operations**
**Task:**  
Perform union, intersection, and difference operations.

**Solution:**
```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

union_set = set1.union(set2)
intersection_set = set1.intersection(set2)
difference_set = set1.difference(set2)

print("Union:", union_set)
print("Intersection:", intersection_set)
print("Difference:", difference_set)
```

#### **Challenge: Set for Membership Testing**
**Task:**  
Check membership in a set of even numbers.

**Solution:**
```python
even_numbers = {2, 4, 6, 8, 10}
number = 6

if number in even_numbers:
    print(f"{number} is in the set.")
else:
    print(f"{number} is not in the set.")
```

---

### **3. Real-World Applications**

#### **Application 1: Student Grades Management**
**Task:**  
Calculate average grades for students.

**Solution:**
```python
grades = {"Alice": [90, 85, 88], "Bob": [75, 80, 70], "Charlie": [100, 95, 98]}

for student, scores in grades.items():
    average = sum(scores) / len(scores)
    print(f"{student}'s average grade: {average}")
```

#### **Application 2: Inventory Tracker**
**Task:**  
Manage product inventory.

**Solution:**
```python
inventory = {"apples": 50, "oranges": 30}

# Add a product
inventory["bananas"] = 20

# Update quantity
inventory["apples"] += 10

# Check stock
product = "oranges"
if product in inventory:
    print(f"{product} is in stock with {inventory[product]} units.")
else:
    print(f"{product} is not in stock.")

print("Updated Inventory:", inventory)
```

#### **Application 3: Keyword Deduplication**
**Task:**  
Remove duplicate keywords.

**Solution:**
```python
keywords = ["python", "coding", "python", "tutorial", "coding"]
unique_keywords = set(keywords)

print("Unique Keywords:", unique_keywords)
```

---

### **4. Challenges to Solve Independently**

#### **Challenge 1: Social Media Analytics**
**Solution:**
```python
hashtags = ["#python", "#AI", "#machinelearning", "#AI", "#coding", "#python"]
hashtag_count = {}
unique_hashtags = set()

for tag in hashtags:
    hashtag_count[tag] = hashtag_count.get(tag, 0) + 1
    unique_hashtags.add(tag)

print("Hashtag Count:", hashtag_count)
print("Unique Hashtags:", unique_hashtags)
```

#### **Challenge 2: Library System**
**Solution:**
```python
library = {"1984": True, "Brave New World": False, "Fahrenheit 451": True}

# Add a book
library["The Great Gatsby"] = True

# Check availability
book = "1984"
if book in library and library[book]:
    print(f"{book} is available.")
else:
    print(f"{book} is not available.")

# Borrow a book
library[book] = False
print("Updated Library:", library)
```

#### **Challenge 3: Student Enrollments**
**Solution:**
```python
class1 = {"Alice", "Bob", "Charlie"}
class2 = {"Bob", "David", "Eve"}

both_classes = class1.intersection(class2)
only_one_class = class1.symmetric_difference(class2)
all_students = class1.union(class2)

print("Both Classes:", both_classes)
print("Only One Class:", only_one_class)
print("All Students:", all_students)
```

#### **Challenge 4: Real Estate Listings**
**Solution:**
```python
listings = ["123 Elm St", "456 Oak St", "123 Elm St", "789 Pine St", "456 Oak St"]
unique_listings = set(listings)

print("Unique Listings:", unique_listings)
print("Total Unique Listings:", len(unique_listings))
```

---
