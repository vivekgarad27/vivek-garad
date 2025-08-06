##WAP to calculate selling price of book based on cost price and discount

cost_price = int(input("Enter cost price:"))
discount = int(input("Enter discount: "))

selling_price = cost_price - (cost_price * discount / 100)

print(f"selling price of book is {selling_price}.")
