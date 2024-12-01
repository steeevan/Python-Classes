
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
