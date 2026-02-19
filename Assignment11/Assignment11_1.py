'''
1. Write a program which accepts one number and checks whether it is prime or not.
Input: 11
Output: Prime Number
'''

import sys

def check_prime_number(no):
    if no < 1:
        print("Not a prime number")
    else:
        is_prime = True    
    for i in range(2,no):
        if (no%i == 0):
            is_prime=False
            break
        i = i+1
    if is_prime:
        print("Prime Number")
    else:
        print("Not a prime number")

if __name__ == "__main__":
    args = sys.argv
    try:
        check_prime_number(int(args[1]))
        #print(result)
    except Exception as e:
        print("Pass the valid number for prime number check") 