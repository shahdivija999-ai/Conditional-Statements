cost=int(input("Enter the cost of the item"))
sell=int(input("Enter the selling price of the item")) 
if sell>cost:
    profit=sell-cost
    print("Profit is"profit)
else: 
    print("No profit")