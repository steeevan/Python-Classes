# ===============================================
# Lesson Plan: Working with Strings in Python
# ===============================================

# **Objective:** Cover string manipulation, string methods, and formatting in Python.

# ===============================================
# 1. Introduction to Strings
# ===============================================

# Strings are sequences of characters in Python. They are used to represent text and are a fundamental data type.

# ===============================================
# 2. Creating Strings
# ===============================================

# Strings can be created using single quotes (''), double quotes (" "), or triple quotes (''' ''') for multi-line strings.

# Examples:
single_quoted = 'Hello, World!'
double_quoted = "Python Programming"
multi_line = '''
This is a multi-line string.
It can span across multiple lines.
'''

# ===============================================
# 3. String Manipulation
# ===============================================

# - Concatenation: Combining two or more strings using the + operator.
# - Repetition: Repeating a string using the * operator.

# Examples:
first_name = "John"
last_name = "Doe"

full_name = first_name + " " + last_name
greeting = "Hello, " + full_name

repeated_text = "Repeat " * 3  # Repeats "Repeat " three times

# ===============================================
# 4. String Methods
# ===============================================

# Python provides various string methods for string manipulation:

# - len(): Returns the length of a string.
# - lower(): Converts a string to lowercase.
# - upper(): Converts a string to uppercase.
# - strip(): Removes leading and trailing whitespace.
# - split(): Splits a string into a list of substrings.
# - join(): Joins a list of strings into one string.
# - find(): Searches for a substring and returns its index.
# - replace(): Replaces a substring with another string.

# Example:
text = "   Python Programming   "
length = len(text)
lower_text = text.lower()
upper_text = text.upper()
stripped_text = text.strip()
word_list = text.split()
new_text = " | ".join(word_list)
index = text.find("Programming")
replaced_text = text.replace("Python", "Java")

# ===============================================
# 5. String Formatting
# ===============================================

# String formatting allows you to create strings with placeholders and fill them with values.

# Examples:
name = "Alice"
age = 30
formatted_text = f"My name is {name} and I am {age} years old."
pi = 3.14159
formatted_pi = f"Pi is approximately {pi:.2f}"  # Formatting with 2 decimal places

# ===============================================
# 6. Additional Examples
# ===============================================

# Example 1: Counting Characters
text = "Python is fun!"
count_e = text.count("e")
print("Number of 'e' characters:", count_e)

# Example 2: Reversing a String
text = "Python"
reversed_text = text[::-1]
print("Reversed string:", reversed_text)

# Example 3: Checking for Substring
email = "user@example.com"
if "@" in email and "." in email:
    print("Valid email address.")
else:
    print("Invalid email address.")

# Example 4: Removing Whitespace
input_text = "  This is some input text.  "
cleaned_text = input_text.strip()
print("Cleaned text:", cleaned_text)

# ===============================================
# 7. Exercises
# ===============================================

# Exercise 1: Create a program that takes a user's first name and last name as input and prints a personalized greeting.
# Exercise 2: Write a program that counts the number of vowels in a given string.
# Exercise 3: Format a message that displays the current date and time in a readable format.
# Exercise 4: Remove any leading and trailing spaces from a given string.

# ===============================================
# 8. Conclusion
# ===============================================

# In this lesson, you've learned how to work with strings in Python, including string manipulation, string methods, and string formatting. Strings are essential for handling text data in various programming tasks.

# Continue practicing with strings to become proficient in working with textual data in your Python programs.

# ===============================================
# Vocabulary Words and Definitions
# ===============================================

# - String: A sequence of characters used to represent text.
# - Concatenation: Combining multiple strings into one.
# - Placeholder: A special symbol or syntax used to represent values that will be inserted into a string.
# - Formatting: The process of creating formatted strings with placeholders.
