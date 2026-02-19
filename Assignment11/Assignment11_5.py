'''
5. Write a program which accepts one number and checks whether it is palindrome or not.
Input: 121
Output: Palindrome
'''

import sys

def check_pallindrom_number(str):
    iter = len(str)
    reverse_str = ''
    while(iter>0):
        iter = iter - 1
        reverse_str = reverse_str +str[iter]
    
    return reverse_str     
        
    
if __name__ == "__main__":
    args = sys.argv
    try:
        rev_str = check_pallindrom_number(args[1])
        if rev_str == args[1]:
            print("Palindrom number")
        else:
            print("Not Pallindrom")    
        
    except Exception as e:
        print("Pass the valid number for palindrom check") 