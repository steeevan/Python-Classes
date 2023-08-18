
#Working with Strings
name = "Magikid"

print(name)

#Print out the First Letter of the Name
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
print(name[5])
print(name[6])

firstHalf = name[0:4]
secondHalf = name[4:7]
print("This is the first half: " , firstHalf)
print("This is the second half: ", secondHalf)

#Concatenation of strings
# kidmagi

thirdSample = secondHalf + firstHalf
print(thirdSample)

# len Function
print(len(name) , "letters")

#Convert Cases
#UPPERCASE or lower case
name2 = name


#Convert to upercase
name2 = name2.upper()
print(name2)

#Convert to lowercase
name2 = name2.lower()
print(name2)

#Capitalizing first letter
name2 = name2.capitalize()
print(name2)

#Counter occurences
phrase = "She sells seashells by the seashore"
countA = phrase.count("se")
print("The total count of 'se' is" , countA)

#Find the number of occurences for ll
countB = phrase.count("ll")
print("The total count of 'll is" , countB)
#Find the number of occurences for as
countC = phrase.count("as")
print("The total count of 'as' is" , countC)
#Find the number of occurences for e
countD = phrase.count("e")
print("The total count of 'e' is" , countD)


#Finding substrings(a section of an entire string)
phrase2 = "Python is a popular programming language in the world."
pos = phrase2.find("language")
print(pos)

pos2 = phrase2.find(" in ")
print(pos2)

substring = phrase2[pos:pos2]
print(substring)

#Acquire the popular word from phrase into a variable substring2
pos3 = phrase2.find("popular")
pos4 = phrase2.find("programming")

substring2 = phrase2[pos3:pos4]
print(substring2)

#Replace substrings
new_phrase = phrase2.replace("world" , "class")
print(new_phrase)

#Proper string formatting
name = "Magikid"
year = 2023
print("We are in" , name , "in the year of" , year)

#Basic method

print("We are in {} in the year of {}".format(name, year))

#F-strings
print(f"We are in {name} in the year of {year}")

#Specifying Decimal places
pi = 3.14159
print("The value of pi is {:.3f}".format(pi))

#Exercise1
var = "Today there are many things in life, that require things to do in the world"
word1 = var.count("thing")
print(f"The number of occurences of 'thing' is {word1}")
word2 = var.count(",")
print(f"The number of occurences of ',' is {word2}")
word3 = var.count("''")
print(f"The number of occurences of '' is {word3}")

#Exercise2
sample = "I am walking around with my family and peeps. Please take a look at the animals in front."
new_sample = sample.replace("a","e")
new_sample = sample.replace("e","i")
new_sample = sample.replace("i","o")
new_sample = sample.replace("o","u")
print(f"This is the new sample {new_sample}")

#Exercise3
sentence = "today I am holding down the house with my axe"
print("This is the original sentence: " , sentence)
example1 = sentence.split()
example2 = [example1[0].capitalize(), example1[1].capitalize(),example1[2].capitalize(),example1[3].capitalize(),example1[4].capitalize(),example1[5].capitalize(),example1[6].capitalize(),example1[7].capitalize(),example1[8].capitalize(),example1[9].capitalize()]
print(example1)
print("This is the revised sentence: ", example2)

#Exercise4
letters = "ABCDEFG"
lowercase = letters.lower()
print(lowercase)

#Exercise5
string = "Life has been going great!"
rev_str = string[::-1]
print(rev_str)































