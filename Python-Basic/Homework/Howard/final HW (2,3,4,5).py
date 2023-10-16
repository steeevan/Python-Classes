


# EXERCISE 2
print("Hello, Python!")


# Exercise 3
try:
    rectangle_length = int(input("please input the length of the rectangle: "))
    rectangle_width = int(input("please input the width of the rectangle: "))
    answer = rectangle_length * rectangle_width
    print("the area is: ",answer)
except ValueError:
    print("you used the wrong letter")
finally:
    pass


# EXERCISE 4
def calculate_discount(price,discount_percentage):
    calculate_answer = price * (1 - discount_percentage/100)
    print("the price is: ", calculate_answer)
    return calculate_answer



# exercise 5
def calculate_total_cost(item_price, tax_rate, discount_percentage):
    price = item_price * (1 - discount_percentage/100) * (tax_rate/100 + 1)
    return price


