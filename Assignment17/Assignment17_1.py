'''
1.Create on module named as Arithmetic which contains 4 functions as Add() for addition, Sub()
for subtraction, Mult() for multiplication and Div() for division. All functions accepts two
parameters as number and perform the operation. Write on python program which call all the
functions from Arithmetic module by accepting the parameters from user.
'''

from Assignment17.Arithmetic import Add,Sub,Mult,Div

no1 = int(input("Enter No1: "))
no2 = int(input("Enter No2: "))

Border = '*'*30
print(Border)
print(f"Addition : {Add(no1,no2)}")
print(f"Substraction : {Sub(no1,no2)}")
print(f"Multiplication : {Mult(no1,no2)}")
print(f"Division : {Div(no1,no2)}")