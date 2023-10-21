# Data Types | EX1
#boolean = true or False
#function : abs() dict() len()
#float: 4.2, 1.79
#integer = 10
#string = hello


# Printing | #Ex2
print("Hello, python!") #
"""
# Caluclate the area of a rectangle | #Ex3
try:
    L = int(input("Enter L: ")) # Asks user to enter a length
    W = int(input("Enter W: ")) # Asks user to enter a widith
    answer = L*W
    print(answer) # Gets "answer" which holds the LxW, and prints them out
except ValueError: #If user did not enter a right value
    print("Please enter a right number") # prints a error
    
# Calcluating Discounts | EX3
def calculate_discount (price, discount_percentage): # Defining our custom function with parameters
    calculate_discount = price * discount_percentage # Takes the original price and multiplys the discount percentage
    return calculate_discount # returns the function
price = 50 # Defining our price
discount_percentage = 0.2 # Defining our discount percentage
discount = calculate_discount(price, discount_percentage) # Using our variable and putting our function in there with our paramenters
print(discount) # Calculate our final price.
"""
# Calculate total cost w/ tax | Ex6
def calculate_total_cost(item_price,discount ,tax_rate): # Defining our custom function with item_price, discount and tax_rate
    Discounted_price  = item_price * discount # Making our discounted price variable with orginal price * discount percentage
    final_price = Discounted_price + (item_price - Discounted_price) * tax_rate # Final price variable with discount price pl
    return final_price
item_price = 75
discount = 0.2
tax_rate = 0.08
total_cost = calculate_total_cost(item_price, discount, tax_rate)
print(total_cost)



