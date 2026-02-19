'''
7. Write a lambda function using filter() which accepts a list of strings and returns a list of strings
having length greater than 5.
'''

nums = ["cat","dog","girafee","monkey","crocodile","rat"]

lambda_calcuate_length = lambda x : len(x) > 5

print(list(filter(lambda_calcuate_length,nums)))