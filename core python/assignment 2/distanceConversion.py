##WAP to convert distance from feet and inches to meters and centimeters
feet = int(input("Enter distance in feet:"))
inches = int(input("Enter distance in inches:"))
total_inches = inches + (feet * 12)

total_centimeters = total_inches * 2.54

meters = total_centimeters // 100

centimeters = total_centimeters % 100

print(f"distance = {meters} meters \nand {centimeters} centimeters. ")


