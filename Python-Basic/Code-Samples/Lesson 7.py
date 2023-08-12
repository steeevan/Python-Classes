# Working with Strings

name = "Magikid" 

print(name)

# Print out the first letter of name
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])
print(name[6])

# SLice name
firstHalf = name[:4]
secondHalf = name[4:]

print("The first half is: ", firstHalf)
print("The second half is: ", secondHalf)

# concatenation of strings
# kidmagi

thirdSample = secondHalf + firstHalf
print(thirdSample)

# len Functin
print(len(name))

# Convert Cases
# UPPER CASE or lower case
name2 = name

#Convert to upper case
name2 = name2.upper()
print(name2)

# Convert to lower case
name2 = name2.lower()
print(name2)

# Capitlizing first letter
name2 = name2.capitalize()
print(name2)


# Counter occurences
phrase = "She sells seashells by the seashore"

countA = phrase.count("se")
print("The total count of 'se' is -> ", countA)

# find the # of occurences for ll
countA = phrase.count("ll")
print("The total count of 'll' is -> ", countA)

# find the # of occurences of as
countA = phrase.count("as")
print("The total count of 'as' is -> ", countA)

# find the # of occurences of e
countA = phrase.count("e")
print("The total count of 'e' is -> ", countA)



# finding substrings
phrase = "Python is a popular programming language in the world."
pos = phrase.find("language")
print(pos)
pos2 = phrase.find(" in")
print(pos2)

substring = phrase[pos:pos2]
print(substring)


# Assign the word popular from phrase into a variable 'substring2'
pos = phrase.find("popular")
print(pos)
pos2 = phrase.find("programming")
print(pos2)

substring = phrase[pos:pos2]
print(substring)



# Replace substrings
new_phrase = phrase.replace("world", "class")
print(new_phrase)

# string formatting
name = "Magikid"
year = 2023
print("We are in ", name, " in the year ", year)

# Basic method

print("We are in {} in the year {}".format(name,year))

# F-strings
print(f"We are in {name} in the year {year}")

# Specifying decimal places
pi = 3.141592653589793238462643383279502884197
print("The value of pi is {:.4f}".format(pi))




# Exerise 1
# counts the number of occurrences of a specific word in a given string.
# Find the # of occruences of thing
# Find the # of occurences of ,
# Find the # of occurences of ' '
#Print all out in clean format
var = "Today there are many things in life, that require things to do in the thing world"

# Exerise 2
#Given a string, write a program to replace all occurrences 
# of 'a' with 'e', 'e' with 'i', 'i' with 'o', and 'o' with 'u'.
sample = "I am walking around with my family and peeps. Please take a look at the animals in front."

# Exerise 3
# Create a program that converts a given string 
# to "title case", where the first letter of each word is capitalized.
sentence = "today I am holding down the house with my axe"
way1 = sentence.split()
print(way1)
way2 = [way1[0].capitalize(), ]
# Exerise 4
# conver lowercase of all letters 
letters = "ABCDEFG"

# Exerise 5
# takes a user-input string and prints the string reversed.
# Use google

















