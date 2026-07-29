'''
8. Write a lambda function using filter() which accepts a list of numbers and returns a list of numbers
divisible by both 3 and 5.
'''

nums = [1,2,3,4,5,6,7,8,9,10,0,15,30]

lambda_number_divisible_3_5 = lambda x : x%3==0 and x%5==0

print(list(filter(lambda_number_divisible_3_5,nums)))