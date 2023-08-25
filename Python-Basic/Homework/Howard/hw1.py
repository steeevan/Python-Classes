#1
length = int(input("please input the length of rectangular:"))
width = int(input("please input the width of rectangular:"))
area = length*width
print("the area of the rectangular is",area)

#q5
t = int(input("how old are you"))
if t < 18:
  print("no you can not vote")
else:
  print("horray you can vote")

#q6
print("whats the temp in Farenhight at your place?")
t = int(input())
v = (t - 32) * 5/9
print("the temp in Celsius is",v)

#q7
n = list(range(1,41,2))
#for i in range(1,41,2):
  #print(i)
print(n)