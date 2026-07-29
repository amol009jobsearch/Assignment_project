'''
3. Write a program which accept one number from user and return its factorial.
Input : 5 Output : 120
'''

def calculate_factorial(no1):
    fact=1
    for i in range(1,no1+1,1):
        fact = fact * i
    return fact    

no1 = int(input("Enter No1: "))
print(f"Factorial of {no1} is -->> {calculate_factorial(no1)}")