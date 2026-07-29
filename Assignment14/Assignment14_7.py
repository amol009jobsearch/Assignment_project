'''
7. Write a lambda function which accepts one number and returns True if divisible by 5.
'''
#normal function to calculate even or odd

is_divisible_by_5 = lambda no1 : no1%5 == 0

if __name__ == "__main__":
    no1 = float(input("Enter Number1: "))
    result = is_divisible_by_5(no1)
    if result:
        print("Yes {} is divisible by 5".format(no1))
    else:
        print("{} is NOT divisible by 5".format(no1))
