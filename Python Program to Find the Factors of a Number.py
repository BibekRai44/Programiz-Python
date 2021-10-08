def print_factors(a):
    print("The factors of ",a,"are:")
    for i in range(1,a+1):
        if a % i == 0:
            print(i)
num = 400
print_factors(num)