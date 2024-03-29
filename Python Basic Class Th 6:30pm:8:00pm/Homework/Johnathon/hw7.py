#1-2
print('question 1')

for i in range(6):
  print (i**2)
  print (i+i)
  
#3

print('\nquestion 2')
x=0
y=1
print(x)
print(y)
i=0
while i<10:
  z=x+y
  print(z)
  x=y
  y=z
  i+=1
  
#4

a=-1
while a<0:
  num=input("Enter another number")
  a=int(num)
  
print(f'{a} is a postive number.')

#5

wordlist=["Hello", "why", "trees", "apple"]
for h in wordlist:
  print (h.upper())
  
#6

number=int(input("Enter a number"))
numbertwo=1
while number>=numbertwo:
  print (numbertwo)
  numbertwo+=1
