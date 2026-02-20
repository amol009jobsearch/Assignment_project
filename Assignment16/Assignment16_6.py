'''
6.Write a program which accept number from user and check whether that number is positive or
negative or zero.
Input : 11 Output : Positive Number
Input : -8 Output : Negative Number
Input : 0 Output : Zero
'''

def check_positive_neg_zero(no1):
    if no1 == 0:
        print("Zero")
    elif no1 < 0:
        print("Negative Number")
    elif no1 > 0:
        print("Positive Number")
    else:
        print("Not a valid number")


no1 = int(input("Enter Number: "))
check_positive_neg_zero(no1)