##program to find the roots of quadratic equation
a = int(input("Enter the value of a :" ))
b = int(input("Enter the value of b :" ))
c = int(input("Enter the value of c :" ))

sqrt = ((b**2)-(4*a*c))**0.5
res1 = (-b + sqrt) / 2 * a
res2 = (-b- sqrt ) / 2 * a

print(f"the res1 is {res1} and res2 {res2} ")