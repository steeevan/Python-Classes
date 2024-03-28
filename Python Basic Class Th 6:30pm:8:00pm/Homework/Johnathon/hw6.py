#1-3

name="Johnathon Bao"
greeting="Hi, my name is "
greeting2=greeting+name
print (greeting2)
greeting3=greeting+(name[0:9])
print (greeting3)

#4-6

sentence=str(input("Enter a sentence"))
print (len(sentence))
upper=sentence.upper()
lower=sentence.lower()
caps=sentence.capitalize()
counts=sentence.count("e")
if "?" in sentence:
  print ("this sentence has a question mark in it")

#7-9

import datetime

date=datetime.datetime.now()
print(date)

a=5*3
print (f"the result of 5 times 3 is {a}")
