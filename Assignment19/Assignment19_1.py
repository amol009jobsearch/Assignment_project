'''
1.Write a program which contains one lambda function which accepts one parameter and return
power of two.
Input : 4 Output : 16
Input : 6 Output : 64
'''

lambda_power = lambda no: no*no

no = int(input("Enter number: "))

print(f"power of {no} is --> {lambda_power(no)}")