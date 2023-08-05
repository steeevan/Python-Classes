# Lesson 6 List and Tuples

# List of colors 
'''
colors = ["Blue", "Red", "Green", "Yellow"]

print(colors)

print("Print out 1st element of list: ", colors[0])
print("Print out 2nd element of list: ", colors[1])
print("Print out 3rd element of list: ", colors[1])
print("Print out 4th element of list: ", colors[1])

# Re-assign new colors
colors[0] = "Black"
colors[1] = "White"
colors[2] = "Pink"
colors[3] = " Purple"

print(colors)

#backward indexing
print(colors[-1])
print(colors[-2])
print(colors[-3])
print(colors[-4])

# Checking for elements in list

checkColor = " Red" in colors
print(checkColor)
checkColor = "Purple" in colors
print(checkColor)

# Slicing
SampleColors = colors[:]      # Gets a copy of the list and assings it to variable
print("This is my list named colors: " , colors)
print("This is my list named Samplecolors: ", SampleColors)

#begin:end
halfList = colors[0:2]
print("This is splicing the list from index 1 to index 2: ", halfList)

numbers = [13,2,82,45,20,6,10,78,9,455]

# Exercise 1
# Make a new list named 'section1' that contains values from 2 - 455
section1 = numbers[1:10]
print("Exercise 1", section1)
#Exercise 2
# make a new list accessing the last element of the list
# using backwards indexing
ex2 = [numbers[-1]]
print("Exercise 2: " ,ex2)
# Exercise 3
# Make a new list named 'half' that gets half of the elements from numbers
half = numbers[0:5]
print("Half of the list: ", half)

'''

numbers = [13,2,82,45,20,6,10,78,9,455]

# slice from element 20 and after

# Copying from index 4 and after
nTwenty = numbers[4:]
print(nTwenty)

nTwenty2 = numbers[:5]
print(nTwenty2)

# List Concatenation
concatenation = nTwenty + nTwenty2
print(numbers)
print(concatenation)

# TO find lenght of the list
print("The length of my list numbers is: " , len(numbers))

#Tuples
# THese are created once assigned
# These cannot be modified after they are created
# You may access elements from it but cannont change them
# You cannot add / remove elements from this

tuplesSample = (1,2,3,4,5)
tuplesSample2 = 10,20,30,40,50,

print(tuplesSample)
print(tuplesSample2)
print(tuplesSample[0])

# THis is not valid
# tuplesSample[0] = 10
# tuplesSample.append(10)
# tuplesSample.pop()

# Tuples Concantenation
newTup = tuplesSample + tuplesSample2
print(newTup)

































































