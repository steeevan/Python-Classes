#1

num1=10
num2=5

#2

add=num1+num2
sub=num1-num2
div=num1/num2
mult=num1*num2
rem=0

#3

print ("the sum is", add)
print ("the difference is", sub)
print ("the product is", mult)
print("the quotient is", div)
print("the remainder is", rem)

#4 & 5

if num1==num2:
  print (num1, "=",num2)
else:
  print (num1,"does not equal", num2)
  
if num1>num2:
  print (num1,"is greater than", num2)
else:
  print (num1, "<", num2)
  
if num1>=num2:
  print (num1,"is greater than or equal to", num2)
else:
  print (num1,"is less than or equal to", num2)
  
  #6
  
if num1>0 and num2<10:
  print (num1,"is greater than 0 and", num2,"is less than 10")
elif num1>0 and num2>10: 
  print (num1, "is greater than 0 and", num2,"is greater than 10")
elif num1>0 and num2==10:
  print (num1, "is greater than 0 and", num2,"is equal to 0")
elif num1<0 and num2==10:
  print (num1, "is less than 0 and", num2,"is equal to 0")
elif num1<0 and num2>10:
  print(num1,"is less than 0 and", num2,"is greater than 10")
elif num1<0 and num2<10:
  print (num1, "is less than 0 and", num1,"is less than 10")
