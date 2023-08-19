'''
Class: Python Basic
Time: 5:15pm - 6:45pm
Name: [Student Name]
Date: [date]

Description:
  This file contains examples for lesson 8 which focuses on
  loops such as for loops, and while loops. Some key words would be
  iterations, indexing, reapeats, etc..
'''


# For loops

'''
A for loop is a fundamental control structure in programming that allows you
to repeatedly execute a block of code for a specified number of iterations.
This is typically used for list,tuples,  strings, ranges, or other iterable objects.
The loop continues until all elements in the sequence have been processed. 
THis works for automating simple task. 
'''

'''
# Example 1
for i in range(5):
  print(i)
'''

'''
Here i is a temporary that is only used within the for loop. Its scope its within
the for loop. Range is a function that allows us to repeat until the range is
reached. 
'''

'''
# Prints 5 - 10
for i in range(5,11):
  print(i)


# Prints even numbers from 0 - 10
for i in range(0,11,2):
  print(i)

# Prints odd numbers from 1 - 10
for i in range(1,11,2):
  print(i)


for i in range(101):
  print(i)

# Example 2
# Using for loops for list

colors = ["blue", "black", "red", "Green", "Orange"]

print(colors[0])
print(colors[1])
print(colors[2])
print(colors[3])
print(colors[4])

print("--------------------------------")
for color in colors:
  print(color)
print("--------------------------------")

# Prints backwards
for color in range(4,-1,-1):
  print(colors[color])


'''

# WHile LOOPS

'''
A WHILE loop is a fundamnetal control structire that allows you to repeatedly
execute a block of code as long as a specified condition remains true.
While loops rely on boolean expression to determine if it will repeat
the block of code.

'''
# Exercise 3
counter = 5

while counter >= 0:
  print(counter)
  counter -= 1      #  counter = counter - 1


# We will make a simple guessing game for our user
number = 7


guess = int(input("Enter a number(0-10): "))

while number != guess:
  print("Wrong guess")
  guess = int(input("Enter a number(0-10): "))
  
print("Hooray")

































