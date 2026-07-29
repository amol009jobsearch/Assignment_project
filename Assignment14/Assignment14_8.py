'''
8. Write a lambda function which accepts two numbers and returns addition.
'''
#normal function to calculate even or odd

lambda_add_two_number = lambda no1,no2 : no1+no2

if __name__ == "__main__":
    no1 = float(input("Enter Number1: "))
    no2 = float(input("Enter Number2: "))
    result = lambda_add_two_number(no1,no2)
    if result:
        print("addition of {} and {} is ->> {}".format(no1,no2,result))
