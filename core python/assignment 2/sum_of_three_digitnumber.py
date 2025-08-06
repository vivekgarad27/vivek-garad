##WAP to find the sum of three digit number
num=int(input("Enter a three digit number:"))

hundred = num // 100
ten = (num % 100) // 10
units = num % 10

sum_of_three_digit_number = hundred + ten + units

print(f"sum of three digit number is {sum_of_three_digit_number}.")