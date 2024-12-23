### Python Data Types and List Manipulation Challenges with Solutions

---

#### **Problem 1: Working with User Input**
**Description**:  
- Ask the user to input their favorite color and store it in a variable.
- Ask the user to input their favorite number and store it in a variable.
- Create a message that combines these inputs and print it (e.g., "Your favorite color is blue, and your favorite number is 7.").

**Solution**:
```python
favorite_color = input("Enter your favorite color: ")
favorite_number = int(input("Enter your favorite number: "))
print(f"Your favorite color is {favorite_color}, and your favorite number is {favorite_number}.")
```

---

#### **Problem 2: List Manipulation**
**Description**:  
1. Create a list called `fruits` that contains 5 of your favorite fruits.  
2. Print the third fruit in the list.  
3. Add two more fruits to the list and print the updated list.  
4. Remove the first fruit from the list and print the updated list.

**Solution**:
```python
fruits = ["apple", "banana", "cherry", "date", "elderberry"]
print(fruits[2])  # Print third fruit
fruits.append("fig")
fruits.append("grape")
print(fruits)  # Updated list
fruits.pop(0)  # Remove first fruit
print(fruits)  # Updated list
```

---

#### **Problem 3: Dice Roll Tracker**
**Description**:  
1. Create a list named `dice_rolls` with values `[1, 2, 3, 4, 5, 6]`.  
2. Simulate adding rolls of a dice:
   - Append `4`, `3`, and `6` to the list.
   - Print the updated list.  
3. Remove the last roll from the list and print the updated list.  
4. Print the total number of rolls stored in the list.

**Solution**:
```python
dice_rolls = [1, 2, 3, 4, 5, 6]
dice_rolls.append(4)
dice_rolls.append(3)
dice_rolls.append(6)
print(dice_rolls)  # Updated list
dice_rolls.pop()  # Remove last roll
print(dice_rolls)  # Updated list
print("Total rolls:", len(dice_rolls))  # Count rolls
```

---

#### **Problem 4: Age List**
**Description**:  
1. Create a list called `years` and store the ages of your classmates (e.g., `[9, 10, 8, 12, 11]`).  
2. Print the youngest age.  
3. Print the oldest age.  
4. Print the average age of the list.

**Solution**:
```python
years = [9, 10, 8, 12, 11]
print("Youngest age:", min(years))
print("Oldest age:", max(years))
print("Average age:", sum(years) / len(years))
```

---

#### **Problem 5: Analyzing a Class List**
**Description**:  
1. Create a list called `class_grades` with the following values: `[87, 92, 78, 94, 88]`.  
2. Add grades for two more students: `95` and `89`.  
3. Remove the lowest grade from the list.  
4. Print the highest grade in the list.  
5. Calculate and print the average of all grades in the list.

**Solution**:
```python
class_grades = [87, 92, 78, 94, 88]
class_grades.append(95)
class_grades.append(89)
class_grades.remove(min(class_grades))  # Remove lowest grade
print("Highest grade:", max(class_grades))
average = sum(class_grades) / len(class_grades)
print("Average grade:", average)
```

---

#### **Problem 6: Dynamic List of Friends**
**Description**:  
1. Create an empty list called `friends`.  
2. Ask the user to input the names of 5 friends and add each to the list.  
3. Print the list of friends.  
4. Remove the third friend from the list and print the updated list.

**Solution**:
```python
friends = []
for i in range(5):
    friend = input(f"Enter the name of friend {i + 1}: ")
    friends.append(friend)
print("Friends list:", friends)
friends.pop(2)  # Remove third friend
print("Updated friends list:", friends)
```

---

#### **Problem 7: Reversing Lists**
**Description**:  
1. Create a list of 10 random numbers.  
2. Reverse the list and print the result.  
3. Print the last 3 numbers in the reversed list.

**Solution**:
```python
random_numbers = [15, 7, 23, 9, 1, 30, 18, 4, 12, 25]
random_numbers.reverse()
print("Reversed list:", random_numbers)
print("Last 3 numbers:", random_numbers[:3])
```

---

#### **Challenge 1: Dice Game Simulation**
**Description**:  
1. Create a list called `dice` with values `[1, 2, 3, 4, 5, 6]`.  
2. Simulate rolling the dice 10 times by randomly selecting a number from the list and appending it to a new list called `rolls`.  
3. Print the result of all 10 rolls.  
4. Calculate and print the most common roll in the list.

**Solution**:
```python
import random

dice = [1, 2, 3, 4, 5, 6]
rolls = [random.choice(dice) for _ in range(10)]
print("Rolls:", rolls)
most_common = max(set(rolls), key=rolls.count)
print("Most common roll:", most_common)
```

---

#### **Challenge 2: Age Comparison**
**Description**:  
1. Ask the user to input the ages of Andy and Gerald.  
2. Print the name of the youngest and oldest person.

**Solution**:
```python
andy_age = int(input("Enter Andy's age: "))
gerald_age = int(input("Enter Gerald's age: "))

if andy_age < gerald_age:
    print("Andy is younger.")
elif gerald_age < andy_age:
    print("Gerald is younger.")
else:
    print("They are the same age.")
```

---

#### **Challenge 3: Number Analysis**
**Description**:  
1. Create a list with 15 numbers.  
2. Find and print:
   - The smallest number.  
   - The largest number.  
   - The sum of all the numbers.  
   - The average of the numbers.

**Solution**:
```python
numbers = [15, 23, 8, 42, 17, 9, 33, 12, 29, 5, 11, 19, 40, 6, 28]
print("Smallest number:", min(numbers))
print("Largest number:", max(numbers))
print("Sum of numbers:", sum(numbers))
print("Average:", sum(numbers) / len(numbers))
```

---

#### **Challenge 4: Unique Values**
**Description**:  
1. Create a list called `numbers` with duplicate values (e.g., `[1, 2, 2, 3, 4, 4, 5]`).  
2. Remove duplicate values from the list and print the updated list.

**Solution**:
```python
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = list(set(numbers))
print("Unique numbers:", unique_numbers)
```

---

#### **Challenge 5: Shopping List Manager**
**Description**:  
1. Create a list called `shopping_list` with 5 items.  
2. Ask the user to add 3 more items to the list and update it.  
3. Print the total number of items in the list.  
4. Remove any duplicates from the list.  
5. Sort the list alphabetically and print the final list.

**Solution**:
```python
shopping_list = ["milk", "bread", "eggs", "cheese", "butter"]

# Add 3 items from the user
for i in range(3):
    item = input(f"Add item {i + 1} to the shopping list: ")
    shopping_list.append(item)

print("Total items in the list:", len(shopping_list))

# Remove duplicates
shopping_list = list(set(shopping_list))

# Sort alphabetically
shopping_list.sort()
print("Final shopping list:", shopping_list)
```

--- 
