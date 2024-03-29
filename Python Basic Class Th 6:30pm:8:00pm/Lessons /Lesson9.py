# ===============================================
# Lesson Plan: Dictionaries and Sets in Python
# ===============================================

# **Objective:** Teach the use of dictionaries and sets for efficient data organization and retrieval.

# ===============================================
# 1. Introduction to Dictionaries and Sets
# ===============================================

# Dictionaries and sets are data structures in Python that allow you to store and manipulate data efficiently.

# - Dictionaries store data as key-value pairs, providing quick access to values based on unique keys.
# - Sets store unique elements and are used for tasks like deduplication and membership testing.

# ===============================================
# 2. Creating Dictionaries and Sets
# ===============================================

# Dictionaries are created using curly braces {} or the "dict()" constructor.
# Sets are created using curly braces {} or the "set()" constructor.

# Examples:
student = {
    "name": "Alice",
    "age": 25,
    "grade": "A"
}

colors = {"red", "green", "blue"}

# ===============================================
# 3. Accessing and Modifying Dictionaries
# ===============================================

# You can access dictionary values using keys and modify them as needed.

# Examples:
name = student["name"]
student["age"] = 26

# ===============================================
# 4. Set Operations
# ===============================================

# Sets support common set operations like union, intersection, and difference.

# Examples:
set1 = {1, 2, 3}
set2 = {3, 4, 5}

union_set = set1.union(set2)
intersection_set = set1.intersection(set2)
difference_set = set1.difference(set2)

# ===============================================
# 5. Additional Examples
# ===============================================

# Example 1: Counting Character Occurrences
text = "python programming"
char_count = {}

for char in text:
    if char.isalpha():
        char = char.lower()
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

print("Character count:", char_count)

# Example 2: Creating a Set from a List
fruits_list = ["apple", "banana", "cherry", "apple"]
unique_fruits = set(fruits_list)
print("Unique fruits:", unique_fruits)

# ===============================================
# 6. Exercises
# ===============================================

# Exercise 1: Create a dictionary to store information about a book (title, author, year of publication) and print the book's details.
# Exercise 2: Given a list of numbers, create a set of unique numbers from the list.
# Exercise 3: Write a program that counts and prints the frequency of each word in a given text.

# ===============================================
# 7. Conclusion
# ===============================================

# In this lesson, you've learned about dictionaries and sets in Python, which are essential for efficient data organization and retrieval. Dictionaries provide quick access to data using keys, while sets store unique elements and support various set operations.

# Continue practicing with dictionaries and sets to optimize data manipulation in your Python programs.

# ===============================================
# Vocabulary Words and Definitions
# ===============================================

# - Dictionary: A data structure that stores data as key-value pairs, allowing quick access to values using unique keys.
# - Set: A data structure that stores unique elements and supports set operations like union and intersection.
# - Key: A unique identifier used to access values in a dictionary.
# - Value: Data associated with a key in a dictionary.
# - Union: A set operation that combines two sets and returns the elements present in either or both sets.
# - Intersection: A set operation that returns the common elements between two sets.
# - Difference: A set operation that returns the elements present in one set but not in the other.
