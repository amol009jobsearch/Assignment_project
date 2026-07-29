'''
10. Write a lambda function which accepts three numbers and returns largest number.
'''
#normal function to calculate even or odd

lambda_max_among_three_nos = lambda no1,no2,no3 : no1 if (no1>no2 and no1>no3) else no2 if (no2>no1 and no2>no3) else no3
#lambda_max_among_three_nos = lambda no1,no2,no3 : max(no1,no2,no3)

if __name__ == "__main__":
    no1 = float(input("Enter Number1: "))
    no2 = float(input("Enter Number2: "))
    no3 = float(input("Enter Number3: "))
    result = lambda_max_among_three_nos(no1,no2,no3)
    if result:
        print("max between {}, {} and {} is ->> {}".format(no1,no2,no3,result))
