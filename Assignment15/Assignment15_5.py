'''
5. Write a lambda function using reduce() which accepts a list of numbers and returns the maximum
element.
'''
from functools import reduce
nums = [1,2,3,4,5,6,7,8,9,10]

lambda_odd_numbers = lambda x,y : x if (x > y) else y

print(reduce(lambda_odd_numbers,nums))