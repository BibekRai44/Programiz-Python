num_list=[2,3,5,34,65,85,234,45,81,543]
result=list(filter(lambda x: (x % 9 == 0),num_list))
print("Numbers divisible by 9 are",result)