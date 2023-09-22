# Functions
'''
#keyword to make a function is
def add(x,y):
  return x + y
  
  
print(add(5,3))



number = 10
if number == 5:
  print("Number is 5")
elif number == 10:
  number = 5
else:
  print("otherwise")
  
# continue
for abcdef in range(1,101,2):
  if abcdef == 69:
    continue
  print(abcdef)
  
 ''' 
  
  
# Exercise 1
# With the given list return the index of the number 10
numbers = [1,2,3,4,5,10,5,5,5]
colors = ["red","green","yellow"]

def find_item(TnumList):
  size_of_list = len(TnumList)
  
  for i in range(size_of_list):
    #print(TnumList[i])
    if TnumList[i] == 4:
      return i
    elif TnumList[i] == "yellow":
      print("Hey we found yellow in the list")
      return 0







# Exercise 2
# Define a function that returns the mean of a given list
# Store the returned value into a variable named "mean"

numbers = [10,50,100,60]

numbers2 = [10,30,30,440,55,60,70,80,80,100]

# comment
'''
asfasffa            iugugiuugu
Block commenta
'''

#---------------------------------------------------------
def MEAN(Tlist):
  '''
-------------------------------------------------------------------------  
  Function Name: MEAN
  Description: This function returns the mean of the sum of the given list.
  
  Input: 
    + Tlist : This holds the list given by the user
    
  Output:
    + "mean" : The sum of list divided by the number of integers in list
    
  Local Variables:
    + length : the size of the given list
    + Tsum : Represents the sum of the list
----------------------------------------------------------------------------    
  '''
  length = len(Tlist)
  
  Tsum = 0
  
  for i in range(length):
    Tsum += Tlist[i]
  
  return Tsum / length

#------------------------------------------------------------------------

mean = MEAN(numbers)
mean2 = MEAN(numbers2)

print(mean)

print(mean2)















