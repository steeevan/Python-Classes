#1-3

num1=int(input("Enter a number"))
if num1>0:
  print ("this number is positive")
elif num1==0:
  print ("this number is 0, not positive or negative")
else:
  print ("this number is negative")
  
#4-6

age=int(input("How old are you?"))
if age <=12:
  print ("you are a child")
elif age <=19:
  print ("you are a teenager")
elif age<=59:
  print ("you are an adult")
elif age>=60:
  print ("you are a senior")
  
#The purpose of the statements, elif and if, are to make
#the command work properly. If I do not include "elif", 
#the code would not work properly and would print out 
#everything if I inputted a 60.
