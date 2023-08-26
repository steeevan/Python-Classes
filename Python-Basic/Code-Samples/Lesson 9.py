
# Dictionary and Sets

#Vocabulary

# Dictionary: A collection of key-value pairs where each key
# is unique and associated with a value

# Key: An identifier used to access the value in a dictionary

# Value: The dat associated to the key in a dictionary

# Set: An unordered collection of unique elements


# Dictionary of a persons information

person = {"name":"Patrick","age":5,"city":"Bikini Bottom"}

# Access values within the dictionary

tname = person["name"]
print(tname)

tage = person["age"]
print(tage)

tage = person["city"]
print(tage)


# Change the city to "Salty Splatoon"
person["city"] = "Salty Splatoon"
print(person)

# Add a characteristic to our person such as color"
# name of the key to be "color" value -> the person color

person["color"] = "Pink"
print(person)

# Dictionary Methods

# Getting all the keys
keys = person.keys()
print(list(keys))

# Getting all values
values = person.values()
print(list(values))


print("--------------------------------------")
# getting key-value pairs
pairs = person.items()
print(pairs)



# Exercises 1
# Create a dictionary named "library", 
#"keys" -> name,year,author, rating
# values -> pick anything you want
library = {"name":"Python", "year":2023,"author":"Estevan","rating":10}
print(library)
# Exercises 2
# add a new key "pages" -> integer

library["pages"] = 5
print(library)
#----------------------------------------------------------
# Sets
print("--------------------------------------")


fruits = {"apples","banana","orange"}
print(fruits)


# add/remove

fruits.add("grape")
print(fruits)

fruits.remove("banana")
print(fruits)

# Set operations

set1 = {1,2,3,4}
set2 = {3,4,5,6}


# union of sets

uni = set1.union(set2)
print(uni)

# Intersection of sets

intersection = set1.intersection(set2)
print(intersection)

# difference of sets
diff = set1.difference(set2)
print(diff)

diff = set2.difference(set1)
print(diff)

#Adding multiple items to our set
fruits.update(["Cherry","kiwi"])
print(fruits)

# remove from set
fruits.discard("kiwi")
print(fruits)

















# Exercise  homework
x = [1,6,6,4,3]
summ = 0
for i in x:
  if i % 2 == 0:
    summ += i
print(summ)