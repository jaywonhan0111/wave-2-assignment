import math

a = int(input("value of a:"))
b = int(input("value of b:"))
c = int(input("value of c"))
discriminant = b**2  -4*a*c
if discriminant < 0:
    print("Number of roots: 0")
elif discriminant == 0:
    print("Number of roots: 1" )
    root = (-b + math.sqrt(discriminant)) / (2*a)
    print("value of real root", root)
else:
    print("Number of roots: 2")
    root1 = (-b + math.sqrt(discriminant)) / (2*a)
    root2 = (-b - math.sqrt(discriminant)) / (2*a)
    print("values of real roots", root1, root2)
    



    
