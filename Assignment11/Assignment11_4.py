'''
4. Write a program which accepts one number and prints reverse of that number.
Input: 123
Output: 321
'''

import sys

def reverse_the_string(str):
    iter = len(str)
    reverse_str = ''
    while(iter>0):
        iter = iter - 1
        reverse_str = reverse_str +str[iter]
    
    return reverse_str     
        
    
if __name__ == "__main__":
    args = sys.argv
    try:
        cnt = reverse_the_string(args[1])
        print(cnt)
    except Exception as e:
        print("Pass the valid number for count number of digit") 