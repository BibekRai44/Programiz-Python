def fibo(n):
    if n<=1:
        return n
    else:
        return(fibo(n-1)+fibo(n-2))
totalterms=12
if totalterms<=0:
    print("Enter positive number:")
else:
    print("fibonacci series")
    for i in range(totalterms):
        print(fibo(i))
