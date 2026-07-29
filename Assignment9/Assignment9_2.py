'''
2. Write a program which contains one function ChkGreater() that accepts two numbers
and prints the greater number.
Input: 10 20
Output: 20 is greater
'''

def ChkGreater(no1,no2):
    if no1>no2:
        print(f"{no1} is greater")
    else:
        print(f"{no2} is greater")

no1=10
no2=20
ChkGreater(no1,no2)     