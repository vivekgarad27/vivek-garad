##WAP to to calculate area and perimeter 

length = int(input("Enter length of rectangle: "))
breadth = int(input("Enter breadth of rectangle: "))
radius = int(input("Enter radius of circle: "))

area_rectangle = length * breadth
perimeter_rectangle = 2 * (length + breadth)
area_circle = 3.14 * radius**2
perimeter_circle = 2 * 3.14 * radius

area_of_half_circle = (3.14 * radius**2) / 2
perimeter_of_half_circle = (2 * 3.14 * radius) / 2

total_area = area_rectangle + area_of_half_circle
total_perimeter = perimeter_rectangle + perimeter_of_half_circle

print(f"total area is {total_area} \nand total perimeter is {total_perimeter}")