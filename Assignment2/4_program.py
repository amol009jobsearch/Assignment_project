import sys
a = 10
str_name = "Amol"
height = 5.4

print(f"a = {a}, type = {type(a)}, getsize = {sys.getsizeof(a)}") # 28 bytes where as in java and python it is 4 bytes
print(f"str_name = {str_name}, type = {type(str_name)}, getsize = {sys.getsizeof(str_name)}") # 50 bytes in python
print(f"height = {height}, type = {type(height)}, getsize = {sys.getsizeof(height)}") # 24 bytes in python

'''
The getsizeof method is used to get the size of variable 
integer usually gets 28 byte, float gets 24 byte and string gets 50 byte
'''