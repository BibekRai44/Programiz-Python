def rec_sum(a):
    if a<=1:
        return a
    else:
        return a + rec_sum(a-1)
num=12
if num<0:
    print("Enter positive number:")
else:
    print("The sum of natural numbers using recursion is",rec_sum(num))