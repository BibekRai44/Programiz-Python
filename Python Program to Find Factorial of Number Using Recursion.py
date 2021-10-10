def rec_fac(a):
    if a == 1:
        return a
    else:
        return a*rec_fac(a-1)
num=8
if num<0:
    print("pls enter positive number:")
elif num==0:
    print("The factorial of 0 is 1")
else:
    print("The factorial of num is",rec_fac(num))