'''
10.Write a lambda function using filter() which accepts a list of numbers and returns the count of even
numbers.
'''
from functools import reduce

nums = [1,2,3,4,5,6,7,8,9,10]

lambda_filter_even = lambda x : x%2 ==0
lambda_add_even = lambda x,y : x+y
fil = list(filter(lambda_filter_even,nums))

print(reduce(lambda_add_even,fil))