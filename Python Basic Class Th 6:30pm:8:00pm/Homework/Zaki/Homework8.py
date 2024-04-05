# 1. 2. 3.
PERSON = {
  "name": "ohieinsen",
  "age":  54,
  "city":  "Cincinnati",
  "occopation": "pilot"}
for key, value in PERSON.items():
  print(key  , ' : ', value)


  PERSON[3] = "chino hill"
print (PERSON)
  
  # 4.
inv = {
    "item one": 6,
    "item two": 2123,
    "item three": 720,
    "item four": 71, 
}
# 5.
print (inv)
inv["item five"]= "264"
print (inv)
inv.pop("item one")
print (inv)
#.6
set1 = { 4, 5, 6, 7, 8, 9, }
set2 = {5, 6, 7, 8, 9, 10, }
name = set1.union(set2)
NAME = set1. intersection(set2)
eman = set1.difference(set2)
print name
print NAME
print eman
numlist = [24534, 44, 6543, 97104]
num = set(numlist)
print (numlist)
print (num)
