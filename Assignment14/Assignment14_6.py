'''
6. Write a lambda function which accepts one number and returns True if number is odd
otherwise False.
'''
#normal function to calculate even or odd

is_odd_true = lambda no1: no1%2 == 1

if __name__ == "__main__":
    no1 = float(input("Enter Number1: "))
    result = is_odd_true(no1)
    if result:
        print("Odd")
    else:
        print("Even")    
