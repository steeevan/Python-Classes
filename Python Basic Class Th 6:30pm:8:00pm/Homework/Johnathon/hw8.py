#1-3

a={
  "Name": "Steven",
  "Age": 48,
  "City": "Chino Hills",
  "Occupation": "software engineer"
}
print (a)
print (a["Name"])
print (a["Age"])
print (a["City"])
print (a["Occupation"])

a["Age"]=49
print (a)

#4-5

my_inv={
  "item 1": "5 scissors",
  "item 2": "1 pencil box"
}
my_inv["item 3"]="2 sheets of paper"
my_inv.pop("item 1")
my_inv["item 3"]="3 sheets of paper"
if "item 1" in my_inv:
  print ("item 1","is in the inventory")
else:
  print ("item 1", "is not in the inventory")
print (my_inv)

#6-8

myset1={1,2,3,4}
myset2={3,4,5,6}

b=myset1.union(myset2)
c=myset1.intersection(myset2)
d=myset1.difference(myset2)
print (b)
print(c)
print(d)
this_list={1,1,3,4,24,24,66,23,8,1,2,3}
print (this_list)
