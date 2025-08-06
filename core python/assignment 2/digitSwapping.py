##write a program to swap two digit  using third variable

x =  int(input("Enter the number:"))
y =  int(input("Enter the number:"))

z = x
x = y
y = z

print(f'digits after swapping x: {x} , y: {y}' )