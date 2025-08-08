##WAP to calculate profit or loss
sp = float(input("Enter the selling price:"))
cp = float(input("Enter the cost price:"))
if sp > cp:
    print("Profit is: ", sp - cp)
elif sp < cp:
    print("Loss is: ", cp - sp)
else:
    print("No profit no loss")