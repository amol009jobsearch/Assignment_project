'''
3. Write a lambda function using filter() which accepts a list of numbers and returns a list of odd
numbers.
'''

nums = [0,1,2,3,4,5,6,7,8,9,10]

lambda_odd_numbers = lambda x : x%2 == 1

result = list(filter(lambda_odd_numbers,nums))

print("result = {}".format(result))


for i in result:
    print("i = {}".format(i))
