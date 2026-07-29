'''
1. Write a lambda function using map() which accepts a list of numbers and returns a list of squares of
each number.
'''

nums = [1,2,3,4,5,6,7,8,9,10]

lambda_square_of_num = lambda x : x * x 

map_out = list(map(lambda_square_of_num, nums))

print("map output = {}".format(map_out))