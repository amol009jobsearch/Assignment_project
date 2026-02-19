'''
1. Write a lambda function which accepts one number and returns square of that number.
'''
#NORMAL FUNCTION
def square_of_number(no1):
    if no1:
        return no1*no1         
    else:
        print("either percentage is none or zero")     

# LAMBDA FUNCTIOn
res = lambda no1: no1*no1                

if __name__ == "__main__":
    try:
        no1 = float(input("Enter No: "))
        result = square_of_number(no1)
        res = lambda no1: no1*no1   
        print("Square of number by normal function : {}".format(result))
        print("Square of number by lambda: {}".format(res(no1)))
    except Exception as e:
        print("Enter valid percentage: {}".format(e))