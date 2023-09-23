import random

#Exercises 1
# Create a function named "Sum" which
# takes in 2 paramaters "Tnum1", "Tnum2" which
# returns the sum of the two numbers
'''
def SUM(Tnum1,Tnum2):
     return Tnum1 + Tnum2
     

SUMOFTWO = SUM(1,1)


randNumber = random.randint(1,10)

#print(randNumber)

for i in range(10):
     randNumber = random.randint(1,10)
     randNumber2 = random.randint(1,10)
     print("Random #1: ", randNumber)
     print("Random #2: ", randNumber2)
     RandSum = SUM(randNumber,randNumber2)
     print("The sum of two random ints: ",RandSum)

'''

# From random module we could use a funcion to
# shuffle a list randomly

num = [10,33,40,7,11]
colors = ["red","blue","orange"]
print(num)
print(colors)
# action
random.shuffle(num)
random.shuffle(colors)
print(num)
print(colors)


# Randomly select an element within the list
randItem = random.choice(num)
print(randItem)

for i in range(5):
     randItem = random.choice(num)
     print(randItem)











