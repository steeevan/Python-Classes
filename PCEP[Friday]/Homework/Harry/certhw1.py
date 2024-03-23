# Lists
numbers = [1,2,3,4,5,6,7,8,9] # list with numbers
numbers.append(11) # add 11 to list
numbers.remove(5) # Remove 5 from list
numbers.insert(2,100) # inserting 2 and 100
print(numbers) # print our final numbers with edits

# tuples
fruits = ("apple", " banna", "cherry", "date") # our tuple
print(fruits.index("cherry")) # prints the cherry (cherry is a index)
# Once a element is added, it cannot be changed/modified/removed

# Dictionary

student = { # our dictionary
    "name": "Jame Doe",
    "grade": 99,
    "age": 88
    
}
student["city"] = "New York City" # Adds a city named NYC into our list
print(student) # Prints our dictionary with our added city
student.pop("grade") # removes grade from our dictionary
print(student) #  Prints our dictionary with our removed grade
if "age" in student: # if age exixts in our dictionary, we print "exists", if not we print "does not exists"
    print("Exists")
else:
    print("Does not exist")

# Math ops
a = 10 # A variable named a which holds number 10
b = 15 # B variable named a which holds number 15
print(a+b) # print out a + b
print(a-b)# print out a - b
print(a*b)# print out a * b
print(a/b)# print out a / b
print(a%b)# print out a % b

# Comparison and logical operations

if a == b: # If a = equals b we print "equal", if they are not equal, then we print out "not equal"
    print("Both values equal")
else:
    print("not equal")
if a > b: # If a is greater than b, we print the number that a is holding and comparing to b's number
    print(f"{a} is greater then {b}")
else:
    print(f"{a} is less then {b}")
if a > 5: # If a is greater then 5, we print "a is big" or we print "a is smol"
    print("a is big")
else:
    print("a is smol")
if b <= 10: # If b is less or equal to 10 we print "b" or we print "b is big"
    print("b is smol")
else:
    print("b is big")

# Problem 1
def sum_of_squares(numbers_list):  # Using a custom function to use numbers, and square them. Returns the results. We use 2 lists with different numbers and returns the summary
    total = 0
    for i in numbers:
        total  += i **2
    return total
result = sum_of_squares(numbers)
print ("sum of square:",result)

#problem 2
def common_elements(list1,list2): # If a element exists in list 1 and 2, we print "element exists", using a custom function to help check it for us
    for i in list1:
        if i in list2:
            return True
        return False
list1 = [1,2,3,4,5]
list2 = [1,2,3,4,5]
if common_elements(list1,list2):
    print("elements exists")
else:
    print("no common elements")

#problem 3 
def merge_dicts(dict1,dict2): # We use two dictionaries and merge them with a custom function
    result = dict1.copy()
    result.update(dict2)
    for i in dict1:
        print(i)
    return result
diction1 = {"key":1,"Help": "hshshs"}
diction2 = {"fruit":"apple","randint": 73,"number": 122}
dict_result = merge_dicts(diction1,diction2)
print(dict_result)
