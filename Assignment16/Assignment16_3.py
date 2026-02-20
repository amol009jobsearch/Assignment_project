'''
3. Write a program which contains one function named as Add() which accepts two numbers
from user and return addition of that two numbers.
Input : 11 5 Output : 16
'''

def Add(No1,No2):
    return No1 + No2  


No1 = int(input("Enter No1: "))
No2 = int(input("Enter No2: "))
result = Add(No1,No2)
print(f"Addition of {No1} and {No2} is ::->> {result}")