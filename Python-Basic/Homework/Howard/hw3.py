#Question 1
t = (input("please type a list of numbers and put a space after every number"))
g = []
g = t.split()
print(g)
h = []
for d in g:
  h.append(int(d)*int(d))
print(h)

#question 2
b = ["The Childrens Blizzard, 1888","Lauren Tarshis",2018]
h = b[0]
f = b[1]
d = b[2]
print("the tile is",h)
print("the author is",f)
print("the year is",d)


#qustion 3
l = input("please input a sting")
k = l[::-1]
print(k)

#question 4
t = input(" type name")
h = input(" type age")
print("hello,",t,"!You are",h,"year old")


#BONOUS_----------------------------------------------------------------------------------
print(f"hello, {t}! You are {h} year old")



#question 5
h = input("type a string")
length = len(h)
i =int(input(f"type a start integer(number) should be smaller than {length}"))
m = int(input(f"type a end integer(number) should be bigger than {i}"))
f = h[i:m]
print(f)


#question 6
j = input("type a string")
n = int(input("type a integer(number)"))
k = len(j)
f = j[k-n:k]
print(f)
print(k)

#q9
h = float(input("how much dollars do you have"))
g = float(input("how much exchange rate to RMB do you want"))
j = g*h
print("horray you have RMB",j)

#q10
h = float(input("type a number"))
j = float(input("type another number"))
o = h/j
print("The value of division is {:.3f}".format(o))