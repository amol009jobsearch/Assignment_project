'''
7. Write a program which contains one function that accept one number from user and returns
true if number is divisible by 5 otherwise return false.
Input : 8 Output : False
Input : 25 Output : True
'''
def check_num_divisible_by_5(no):
    is_divisible=False
    if no:
        if no%5 == 0:
            is_divisible=True
    else:
        print("Either no is None or Zero.. Enter Valid number")
    return is_divisible    
    

if __name__ == "__main__":
    no = int(input("Enter Number : "))
    print(check_num_divisible_by_5(no))