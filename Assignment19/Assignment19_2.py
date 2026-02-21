'''
2.Write a program which contains one lambda function which accepts two parameters and return
its multiplication.
Input : 4 3 Output : 12
Input : 6 3 Output : 18
'''

def main():
    lambda_multiply_two_number = lambda x,y : x*y

    no1=int(input("Enter No1: "))
    no2=int(input("Enter No2: "))

    print(f"multiply {no1} and {no2} --> {lambda_multiply_two_number(no1,no2)}")

main()    