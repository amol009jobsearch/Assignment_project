'''
5.Write a program which accept one number for user and check whether number is prime or not.
Input : 5 Output : It is Prime Number
'''

def check_prime_number(no1):
    is_prime = True
    for i in range(2,no1,1):
        if no1%i == 0:
            is_prime=False
    return is_prime        

        

no1 = int(input("Enter No1: "))
result = check_prime_number(no1)
if not result:
    print("NOT Prime Number")
else:
    print("Prime Number")    