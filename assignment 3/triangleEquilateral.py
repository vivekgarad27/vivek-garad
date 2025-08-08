##WAP to check whether the triangle is equilateral , isosceles or salene triangle.
side1 = int(input("Enter side 1:"))
side2 = int(input("Enter side 2:"))
side3 = int(input("Enter side 3:"))
if side1 == side2 == side3:
    print("The triangle is equilateral")
elif side1 == side2 or side2 == side3 or side3 == side1:
    print("The triangle is isosceles")
elif side1 != side2 and side2 != side3 and side3 != side1:
    print("The triangle is scalene.")    
else:
    print("invalid triangle")
    
