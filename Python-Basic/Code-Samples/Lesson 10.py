# Homework Exercises

# Problem 10

# Method 1
#Write a program that takes a list 
# of numbers and removes all duplicates, then prints the updated list.
'''
numbers = [1,2,2,3,4,4,5,6,6,7]

unique = list(set(numbers))

# Method 2
new_list = []
for i in range(len(numbers)):
  if numbers[i] in new_list:
    pass
  else:
    new_list.append(numbers[i])
    
print(numbers)
print(new_list)

# Problem 11

Create a tuple of coordinates representing points (x, y). 
Use a for loop to calculate the distance of each point from 
the origin (0, 0).


coord = (9,5)
zero = (0,0)

x_dist = coord[0] - zero[0]
y_dist = coord[1] - zero[1]

new_coord = (x_dist,y_dist)
print(x_dist)
print(y_dist)
print(new_coord)

list_Coords = [(1,5),(6,2),(3,51),(11,50),(111,45)]

coord_distance = []


for cord in list_Coords:
  x_dist = cord[0] - 0
  y_dist = cord[1] - 0
  new_coord = (x_dist,y_dist)
  coord_distance.append(new_coord)



print(list_Coords)
print(coord_distance)

'''
#-----------------------------------------------------------------------------
#Lesson 10
'''
grades = ["A","B","C","D","F"]

#Apppend
print(grades)
grades.append("I")
print(grades)

#Remove
grades.pop()
print(grades)

grades = tuple(grades)
print(grades)

student = {"name":" ","age":0,"ID":0,"Gender":" "}

print(student)

#Alex Smith
# 11
#00465
# Male

student["name"] = "Alex Smith"
student["age"] = 11
student["ID"] = 465
student["Gender"] = "Male"

print(student)


# Sets
# A set is a built in data structure used to store unordered data/collection
# of unique elements
# This means that a set cannont contain duplicates values. 

# Example 1
# Create a set
my_set = {100,3,2,1}
print(my_set)

for i in my_set:
  print(i)



# Add
my_set.add(5)

print(my_set)

# Remove
my_set.remove(5)
print(my_set)
'''
#**************************************************************************
# Guessing Game Project 

numberC = 22
points = 0
numOfGuesses = 0
print("Welcome to our Guessing Game. You have 0 points, but can get more with each correct guess")

usersGuess = int(input("Enter a number(1-100): "))
numOfGuesses += 1

# make a list to keep track of the numbers that were guessed
list_of_guessNum = []

while numberC != usersGuess:
  if usersGuess in list_of_guessNum:
    print("You already guessed ", usersGuess)
    print("Please enter a new number")
  else:
    print("Hey Wrong Number!")
    list_of_guessNum.append(usersGuess)
  
  
  usersGuess = int(input("Enter a number(1-100): "))
  numOfGuesses += 1

list_of_guessNum.append(usersGuess)
points += 1
print(list_of_guessNum)

print(f"The number of guesses you made were {numOfGuesses}")
# print("The number of guesses you made were ",len(list_of_guessNum))
print(f"The points that you have are {points}")







