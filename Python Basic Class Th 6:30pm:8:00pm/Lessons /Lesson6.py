# ===============================================
# Lesson Plan: Lists and Tuples in Python
# ===============================================

# **Objective:** Introduce lists and tuples, their properties, manipulation, and indexing.

# ===============================================
# 1. Introduction to Lists and Tuples
# ===============================================

# Lists and tuples are data structures in Python that allow you to store collections of values.

# - Lists are mutable, meaning their elements can be changed after creation.
# - Tuples are immutable, meaning their elements cannot be changed after creation.

# ===============================================
# 2. Creating Lists and Tuples
# ===============================================

# Lists are created using square brackets [].
# Tuples are created using parentheses ().

# Examples:
fruits_list = ["apple", "banana", "cherry"]
colors_tuple = ("red", "green", "blue")

# ===============================================
# 3. Accessing Elements
# ===============================================

# Elements in lists and tuples are accessed using indexing.

# Example:
first_fruit = fruits_list[0]
second_color = colors_tuple[1]

# ===============================================
# 4. Manipulating Lists (Mutable)
# ===============================================

# - Adding elements: Use the append() method to add elements to the end of a list.
# - Removing elements: Use the remove() method to remove a specific element by value.
# - Modifying elements: Assign a new value to an element using indexing.

# Examples:
fruits_list.append("orange")  # Adding an element
fruits_list.remove("banana")  # Removing an element
fruits_list[1] = "grape"      # Modifying an element

# ===============================================
# 5. Manipulating Tuples (Immutable)
# ===============================================

# Tuples cannot be modified after creation, so all elements must be defined when creating the tuple.

# Example:
coordinates = (3, 4)

# ===============================================
# 6. Additional Examples
# ===============================================

# Example 1: Slicing Lists
numbers_list = [1, 2, 3, 4, 5]
sliced_list = numbers_list[1:4]  # Slice from index 1 to 3 (exclusive)
print(sliced_list)

# Example 2: Concatenating Lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = list1 + list2
print(combined_list)

# Example 3: Tuple Unpacking
coordinates = (5, 7)
x, y = coordinates
print("x =", x)
print("y =", y)

# Example 4: Finding the Length
num_list = [10, 20, 30, 40, 50]
length = len(num_list)
print("Length of num_list:", length)

# Example 5: Checking for Existence
fruits = ["apple", "banana", "cherry"]
if "banana" in fruits:
    print("Banana is in the list.")
else:
    print("Banana is not in the list.")

# ===============================================
# 7. Exercises
# ===============================================

# Exercise 1: Create a list of your favorite movies. Print the first and last movies in the list.

# Exercise 2: Create a tuple with the coordinates (latitude, longitude) of your current location. Print both coordinates.

# Exercise 3: Given a list of numbers, find and print the maximum and minimum values in the list.

# Exercise 4: Write a program that takes a list of numbers, squares each number, and stores the results in a new list.

# ===============================================
# 8. Conclusion
# ===============================================

# In this lesson, you've learned about lists and tuples in Python. Lists are mutable, while tuples are immutable. You can access elements, manipulate them, and perform various operations to work with collections of data.

# Practice using lists and tuples to store and manipulate data effectively in your programs.

# ===============================================
# Vocabulary Words and Definitions
# ===============================================

# - Lists: Mutable data structures in Python used to store collections of values.
# - Tuples: Immutable data structures in Python used to store collections of values.
# - Indexing: The process of accessing elements in a list or tuple using their position.
# - Mutable: Data structures that can be modified after creation.
# - Immutable: Data structures that cannot be modified after creation.
