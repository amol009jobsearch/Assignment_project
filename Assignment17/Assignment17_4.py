'''
4.Write a program which accept one number form user and return addition of its factors.
Input : 12 Output : 16 (1+2+3+4+6)
'''

def calculate_addition_of_factorial(no1):
    fact=0
    for i in range(1,no1,1):
        #print(f"i = {i}")
        if no1%i == 0:
            print(f"factor : {i}")
            fact = fact + i
    return fact    

no1 = int(input("Enter No1: "))
print(f"addition of Factorial of {no1} is -->> {calculate_addition_of_factorial(no1)}")