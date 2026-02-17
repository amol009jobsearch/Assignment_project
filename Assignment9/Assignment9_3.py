'''
3. Write a program which accepts one number and prints square of that number.
Input: 5
Output: 25
'''

def square_of_number(no1):
    sqr = 0
    if no1:
        sqr = no1*no1
    else:
        sqr = 0
    return sqr

no1=int(input("Enter No1: "))

sqr = square_of_number(no1)
print(f"square of number = {sqr}")     