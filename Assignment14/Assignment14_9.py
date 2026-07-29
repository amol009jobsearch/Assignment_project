'''
9. Write a lambda function which accepts two numbers and returns multiplication.
'''
#normal function to calculate even or odd

lambda_multiplication_two_number = lambda no1,no2 : no1*no2

if __name__ == "__main__":
    no1 = float(input("Enter Number1: "))
    no2 = float(input("Enter Number2: "))
    result = lambda_multiplication_two_number(no1,no2)
    if result:
        print("multipicatoin of {} and {} is ->> {}".format(no1,no2,result))
