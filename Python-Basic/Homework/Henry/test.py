def calculate_total_cost(item_price, discount, tax_rate):
    discounted_price = item_price * discount
    final_price = discounted_price + (item_price - discounted_price) * tax_rate
    return final_price

item_price = 75
discount = 0.2  # 20% discount
tax_rate = 0.08  # 8% tax rate

total_cost = calculate_total_cost(item_price, discount, tax_rate)
print(f"The total cost is ${total_cost:.2f}")
