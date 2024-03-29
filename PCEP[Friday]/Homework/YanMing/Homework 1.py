#Assignment 1
numbers = [1,2,3,4,5,6,7,8,9,10]

numbers.append(11)

numbers.remove(5)

numbers.insert(1,100)

print(len(numbers))

#Assignment 2
fruits = ("apple","banana","cherry","date")

print(fruits[2])

#fruits[1] = "grape"

#Tuples cannot be changed or modified unlike a list.

print(len(fruits))

#Assignment 3
student = {"name":"Yanming","age":10,"grade":5}

student["city"] = "New York"

del student["grade"]

print(student.keys())

if "age" in student:
    print("True")
else:
    print("False")

#Assignment 4
a = 10
b = 5
print(a+b)

print(a-b)

print(a*b)

print(a/b)

print(a%b)

#Assignment 5
print(a == b)

print(a>b)

print(a>b and b <= 10)

#Problem 1
numbers = [10,20,30,40,50]
def sum_of_squares(TList):
    total = 0
    for i in TList:
        i **=2
        total += i
    print(total)
sum_of_squares(numbers)

#Problem 2
firstlist = [1,5,7,3]
secondlist = [1,2,7,2]
def common_elements(TList,TList2):
    common = []
    for i in TList:
        for x in TList2:
            if i == x:
                common.append(i)
    print(common)

common_elements(firstlist,secondlist)

#Problem 3
dict1 = {"color":"blue","mood":"happy"}
dict2 = {"color":"red","mood":"excited"}
def merge_dicts(TDict,TDict2):
    result = {}
    for i in TDict:
        result[i] = TDict[i]
    for i in TDict2:
        if i in result:
            result[i] += TDict2[i]
        else:
            result[i] = TDict2[i]
    print(result)
merge_dicts(dict1,dict2)
















