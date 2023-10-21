#1
integer = 1
#this is a number
string = "hi"
#this is used to be text
floaT = 1.4
#this is a number with a decimal
boolean = True
#this is used to represent true or false
#-----------------------------------------
#2
print("Hello, Python!")
#-------------------------
#3
try:
    width = int(input("what is the width of your rectangle?: "))
    lengh = int(input("what is the lengh of your rectangle?: "))
    area = width * lengh
    print(area)

except ValueError:
    print("you need to make a number that is one charecter")
#----------------------------------------------------------------
#4
def discount_percentage(price, discount):
    total = price - discount * price - price 
    print(total)
    print("this is how much money you should subtract o the original price to get your total")
    return discount_percentage

price = float(input("what is the price?: "))
discount = float(input("what is the discount?: "))
print(discount_percentage(price, discount))
#-----------------------------------------------------------------
#5
def caculate_total_cost(item_price, discount_Percentage, tax_rate):
    Total = item_price - discount_Percentage * item_price - price - (tax_rate / 100 * item_price)
    print(Total)
    print("this is how much you should minus to the original price to get your total")
    return caculate_total_cost
item_price = float(input("what is the price?: "))
discount_Percentage = float(input("what is the discount?: "))
tax_rate = float(input("what is the tax rate"))
print(caculate_total_cost(item_price, discount_Percentage, tax_rate))
#------------------------------------------------------------------------------------------
#6
#variable scope specifies the place where we get a variable
#function perameter is the variable thats its in something like a def block
#return statement is used to get the output of a def block
#syntax error is where we made a mistake wriing the code
#data type conversion is where you convert like a string number to a integer
