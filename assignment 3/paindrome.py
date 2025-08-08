##WAP to check if given 3 digit number is a palindrome or not.
num = int(input("Enter three digit number:"))

temp = num

digit1 = temp % 10
temp = temp // 10

digit2 = temp % 10
temp = temp // 10 

digit3 = temp % 10
temp = temp // 10

reversed_number = digit1 * 100 + digit2 * 10 + digit3

if(reversed_number == num):
    print(f"{num} is palindrome.")
else:
    print(f"{num} is not palindrome.")