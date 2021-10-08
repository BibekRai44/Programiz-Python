def find_hcf(a,b):
    if a>b:
        smaller=a
    else:
        smaller=b
    for i in range(1,smaller+1):
        if((a % i == 0)and (b % i == 0)):
            hcf=i
    return hcf
num1=64
num2=44
print("The HCF is ",find_hcf(num1, num2))