##WAP to input electricity unit charges and calculate total electricity bill according to given condition:
#for first 50 units Rs. 0.50/unit
#for next 100 units Rs. 0.75/units
#for next 100 units Rs. 1.20/units
#for unit above 250 Rs. 1.50/unit
#An additional surcharge of 20% is added to the bill.

units = int(input("Enter units: "))

total_bill = 0
if units > 0:
    if units <= 50:
        total_bill = units * 0.50
    elif units <= 150:
        total_bill = (50 * 0.50) + ((units - 50) * 0.75)
    elif units <= 250:
        total_bill = (50 * 0.50) + (100 * 0.75) + ((units - 150) * 1.20)
    else:
        total_bill = (50 * 0.50) + (100 * 0.75) + (100 * 1.20) + ((units - 250) * 1.50)
    
    total_bill = total_bill + (total_bill * 0.2)
    print(f"Total electricity bill: Rs. {total_bill}")
else:
    print("Invalid input \nUnits must be positive.")
