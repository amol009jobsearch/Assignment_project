'''
5. Write a lambda function which accepts one number and returns True if number is even
otherwise False.
'''
#normal function to calculate even or odd

is_even_true = lambda no1: no1%2 == 0

if __name__ == "__main__":
    print("")
    no1 = float(input("Enter Number1: "))
    result = is_even_true(no1)
    if result:
        print("Even")
    else:
        print("Odd")    
