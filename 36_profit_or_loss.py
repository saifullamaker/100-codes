"""
Problem 36: Profit or Loss
Statement: Read the cost price and selling price -- print profit, loss, or no profit no loss
"""

cost_price = float(input("Enter Cost Price: "))
selling_price = float(input("Enter Selling Price: "))

if selling_price > cost_price:
    profit = selling_price - cost_price
    print("Profit of:", profit)
elif cost_price > selling_price:
    loss = cost_price - selling_price
    print("Loss of:", loss)
else:
    print("No Profit No Loss")
