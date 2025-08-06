##WAP to calculate area of triangle and rectangle
#area of triangle = 0.5 * base * height
#area of rectangle = length * breadth

base = int(input("Enter base of triangle:"))
height = int(input("Enter height of triangle:"))

length = int(input("Enter length of rectangle:"))
breadth = int(input("Enter breadth of rectangle:"))

area_of_triangle = 0.5 * base * height

area_of_rectangle = length * breadth

print(f"Area of triangle: {area_of_triangle} \nArea of rectangle: {area_of_rectangle}.")