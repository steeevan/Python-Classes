# ===============================================
# Lesson Plan: Lists, Tuples, Dictionaries, and Sets in Python
# ===============================================

# **Objective:** Cover methods to use and access Lists, Tuples, Dictionaries, and Sets, 
# along with their properties, manipulation, and indexing.

# ===============================================
# 1. Introduction to Lists, Tuples, Dictionaries, and Sets
# ===============================================

# Lists, Tuples, Dictionaries, and Sets are versatile data structures in Python, 
# each serving specific purposes.

# - Lists: Ordered collections of values that can be modified (mutable).
# - Tuples: Ordered collections of values that are immutable (cannot be changed after creation).
# - Dictionaries: Collections of key-value pairs for efficient data retrieval.
# - Sets: Collections of unique elements for deduplication and membership testing.
# ===============================================
# 2. Creating Lists and Tuples
# ===============================================

# Lists are created using square brackets [].
# Tuples are created using parentheses ().

# Examples:
fruits_list = ["apple", "banana", "cherry"]
colors_tuple = ("red", "green", "blue")


# ===============================================
# 3. Accessing and Modifying Lists and Tuples
# ===============================================

# Elements in lists and tuples are accessed using indexing.

# Examples:
first_fruit = fruits_list[0]
second_color = colors_tuple[1]

# Lists can be modified, but tuples cannot.

# ===============================================
# 4. Dictionary Operations
# ===============================================

# Dictionaries store data as key-value pairs.

# Examples:
student = {
    "name": "Alice",
    "age": 25,
    "grade": "A"
}

name = student["name"]
student["age"] = 26

# ===============================================
# 5. Set Operations
# ===============================================

# Sets store unique elements.

# Examples:
set1 = {1, 2, 3}
set2 = {3, 4, 5}

union_set = set1.union(set2)
intersection_set = set1.intersection(set2)
difference_set = set1.difference(set2)



# ===============================================
# 6. Additional Examples
# ===============================================

# Example 1: Slicing Lists
numbers_list = [1, 2, 3, 4, 5]
sliced_list = numbers_list[1:4]  # Slice from index 1 to 3 (exclusive)

# Example 2: Concatenating Lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined_list = list1 + list2

# Example 3: Creating a Set from a List
fruits_list = ["apple", "banana", "cherry", "apple"]
unique_fruits = set(fruits_list)


# ===============================================
# 7. Exercises
# ===============================================
'''
# Exercise 1: Create a program that takes a user's 
# first name and last name as input and prints a personalized greeting.

#output: Estevan Anguiano welcomes you to his python class!
name = input("Enter your first and last name: ")
print(name, " Welcome to my coding class!")


# Exercise 2: Given a list of numbers, create a set of unique numbers from the list.
numbersList = [10,20,10,20,30,40,50,60,10,100,10,20,40,1,1,10]
unique_set = set(numbersList)
print(unique_set)

'''
# Code problem
# Given the number to guess, we will repeatedly guess until we guess the correct number
# THen ouput the number of times it took for you to guess correctly.
#[Optional]: given the max number of tries, if larger then we stop and player loses
correct_number = 15
guess_list = []
# Optional
max_num_guess = 5
winner_bool = False

guesses_number = int(input("Guess the number: "))
guess_list.append(guesses_number)

#counter = 1
while guesses_number != correct_number and len(guess_list) < 5:
  print("OOF Wrong Number!")
  guesses_number = int(input("Guess again: "))
 # counter += 1 # counter = counter + 1
  guess_list.append(guesses_number)
  
if len(guess_list) <  5:
  print("Yay you guessed correctly! The number was ",correct_number)
  print("It took you ",len(guess_list), " tries to guess correctly!")
  print("Here are all your guess including your correct guess:", guess_list)
else:
  print("HA you loser! You couldnt guess the number!")
  print("THe number was ", correct_number, " and here are your guesse: ", guess_list)
  print("Try next time buddy!")
  
  
  
  
# ===============================================
# 8. Conclusion
# ===============================================

# In this lesson, you've learned about Lists, Tuples, Dictionaries, and Sets in Python. Lists and Tuples allow you to store ordered collections of data, Dictionaries provide efficient data retrieval using keys, and Sets are used for deduplication and membership testing.

# Continue practicing with these data structures to enhance your data manipulation skills in Python.

# ===============================================
# Vocabulary Words and Definitions
# ===============================================

# - List: An ordered collection of values that can be modified (mutable).
# - Tuple: An ordered collection of values that is immutable (cannot be changed after creation).
# - Dictionary: A collection of key-value pairs for efficient data retrieval.
# - Set: A collection of unique elements used for deduplication and membership testing.
