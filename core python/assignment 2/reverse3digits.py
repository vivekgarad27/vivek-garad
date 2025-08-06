#WAP to reverse three digit number
num=int(input("Enter a three digit number:"))

hundred = num // 100
tens = (num % 100) // 10
units = num % 10

hundred,units = units,hundred

reversed_number = hundred * 100 + tens * 10 + units

print(f"Reversed number is : {reversed_number}" )
