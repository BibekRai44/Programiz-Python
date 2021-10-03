import cmath
b=8
c=6
a=3
d=(b**2)-(4*a*c)
solution1 = (-b-cmath.sqrt(d))/(2*a)
solution2 = (-b+cmath.sqrt(d))/(2*a)
print("The solution are {0} and {1} ".format(solution1,solution2))