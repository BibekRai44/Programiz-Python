a=10
fac = 1
if a<0:
    print("sorry, negative numbers do not have factorial")
elif a == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1,a+1):
        fac=fac*i
    print("The factorial of",a,"is",fac)