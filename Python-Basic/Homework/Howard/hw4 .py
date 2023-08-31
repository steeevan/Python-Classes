#problem1question1
h = int(input("type a number"))
for k in range(1,h+1):
  g = k*h
  print(k,"*",h,"=",g)

# problem2question 2
g = [1,5,3,4,2,8,9,5,6,8]
r = 0
for a in g:
   if a % 2 == 0:
     r += a
print(r)

#problem2question3
h = ["teddy", "huston", "jeffrey","bruce"]
k = []
for j in h:
  k.append(j.upper())
print(k)

#problem2 question4
h = (1,2,3,4,55,6,7,767,353,6,736,767,745,6,3,6,68,77,5,65,6,345,45,425,4,5)
k = []
for j in h:
  k.append(j*j)
print(k)

#problem 3 question 5
p = ("hamburgers", "hotdogs", "pizza", "chicken legs", "chicken wings")
print(len(p))

#problem 3 question 6
p = float(input("what the temp over there in Celsius"))
h = (p * 9/5) + 32
print("the temp in fahrenheit is ",h)

#problem 4 question 7
import random
n = random.randrange(1,10)
guess = int(input("Enter any number: "))
while n!= guess:
    if guess < n:
        print("Too low")
        guess = int(input("Enter number again: "))
    elif guess > n:
        print("Too high!")
        guess = int(input("Enter number again: "))
    else:
      break
print("you guessed it right!!")

#there is no question 8

#problem 5 question 9
p = ["hamburgers", "hotdogs", "pizza", "chicken", "legs", "wing"]
l = []
for j in p:
  if len(j)>5:
    l.append(j)
print(l)

#problem5 question10
l = [1,3,2,5,1,5,3,6,4,4,6,7]
o = []
#i check every number in l , if it is in o already then don't put into o
for j in l:
  if j in o:
    continue
  else:
    o.append(j)
print(o)


#question 11 I haven't learned this yet in math

#problem7 question12
import random
y = []
for u in range(20):
 n = random.randrange(1,50)
 y.append(n)
print(y)

h = 0
for e in y:
 if e > h:
   h = e
print(h)

for e in y:
 if e < h:
   h = e
print(h)

#problem8 question13
f = [5,3,4,5]
for x in f:
  for y in f:
    print(y*x)
    
#problem9 question14
q = [1,4,-3,43,56,7,94,3,6,-18,15,89]
for w in q:
  if w <= 12 and w >= 0:
    print("you are a child")
  elif w <= 19 and w >= 13:
    print("you are a teen") 
  elif w <= 65 and w >= 20:
    print("you are a adult")
  elif w >= 66:
    print("you are a senior")
  else:
    print("the age is not avalible")
    
#problem10 question15
import random
y = []
for u in range(10):
 n = random.randrange(1,20)
 y.append(n)
print(y)
q = 0
for h in y:
  if h == 15:
    print("there is a",h)
    q += 1
    print("it is in the place of",q)
    break
  else:
    q += 1
if q == 10:
 print("no 15 avalible (not in the list)")
