highest=3000
lowest=2000
print("prime numbers between",highest,"and",lowest,"are:")
for num in range(lowest,highest+1):
    if num >1:
        for i in range(2,num):
            if (num%i)==0:
                break
        else:
            print(num)
