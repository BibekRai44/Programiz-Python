my_str="BIBEKkebib"
my_str=my_str.casefold()
rev_str=reversed(my_str)
if list(my_str)==list(rev_str):
    print("The string is palindrome")
else:
    print("The string is not palindrome")