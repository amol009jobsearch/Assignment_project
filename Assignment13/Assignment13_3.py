'''
3. Write a program which accepts one number and checks whether it is perfect number or
not.
Input: 6
Output: Perfect Number
'''

def check_perfect_number(no1):
    is_perfect=False
    if no1:
        sum = 0
        for i in range(1,no1,1):
            if no1 % i == 0:
                print(i)
                sum = sum + i
        if no1 == sum:
            is_perfect=True
    else:
        print("either no1 is none or zero")
    return is_perfect         

if __name__ == "__main__":
    No1 = int(input("Enter Number: "))
    result = check_perfect_number(No1)
    if result:
        print(f"{No1} is perfect number")
    else:
        print("Not a perfect number")    