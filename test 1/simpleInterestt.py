##WAP to calculate simple interest
#Simple Interest = (Principal * Rate * Time) / 100

p = int(input("Enter principle amount:"))
r = int(input("Enter rate of interest:"))   
t = int(input("Enter time period:"))

si = ( p * r * t ) / 100

print(f"simple interest of amount : {si}")