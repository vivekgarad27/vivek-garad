##WAP to input all sides of triangle and check whether triangle is valid or not.
a = int(input("Enter side 1:"))
b = int(input("Enter side 2:"))
c = int(input("Enter side 3:"))
if a + b > c and a + c > b and b + c > a:
    print("this is valid triangle.")
else:
    print("this is invalid triangle.")
