import cmath
a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))
d = (b*b) - (4*a*c)
sol1 = (-b+cmath.sqrt(d))/(2*a)
sol2 = (-b-cmath.sqrt(d))/(2*a)
print("The solutions are", sol1, "and", sol2)
