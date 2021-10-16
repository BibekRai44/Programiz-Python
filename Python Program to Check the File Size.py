import os
file_stat=os.stat('python notepad.txt')
print(file_stat.st_size)