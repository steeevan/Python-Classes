# Exercise 1 
# Conditional Statements and List
# we will learn new printing method

name = "Estevan Anguiano"
age = 25
birthyear = 1998

print("Hi my name is " , name , age, birthyear)
print("I am ", age, " years old.")
print("I was born in the year of " , birthyear)

print(f"Hi my name is {name} {age} {birthyear}")
print(f"I am {age} years old.")
print(f"I was born in the year of {birthyear}")

#----------------------------------------------------------------
# Exercise 2
# Condtional Statements


  grade = int(input("Enter the grade for the student(1-100 %): "))
  
  if grade >= 90:
    print("YAY good job on getting an A")
  elif grade <= 89 and grade >= 80:
    print("Good you got a B")
  elif grade <= 79 and grade >= 70:
    print("C")
  elif grade< = 69 and grade >= 60:
    print("D")
  else:
    print("F")
    print("Horrible! I will speak with you privately after class! -.- ")
  


#-----------------------------------------------------------------------
# exercise 3
# Working and comparing values in list
numbers = []

while True:
  entry = int(input("Enter a number"))
  if entry == 0:
    break
  numbers.append(entry)
  print(numbers)
  
print("Loop has been broken!")
print(numbers)

numberSearch = int(input("Enter a number you are searching for: ")) 
if numberSearch in numbers:
  print("I found the number in the list")
else:
  print("I did not find the number")
  
  
# Problem 1
# Create a variable age and if the person enters age that is less 4 then 
# they are babies
# else if they are between 4 and 12 they are kids
# else if they are between 13 and 17 they are teens
# and if they are greater than or equal to 18 then they are adults.


#Problem 2
# make a variable of list type that holds [10,15,20,25,25,100]
# check if the values 1 , 4, 20, and 25 are in the list and if they 
#are then show which ones are in the list and whic
# are not

  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  

