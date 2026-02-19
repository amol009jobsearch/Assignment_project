'''
3. Write a program which accepts one number and prints sum of digits.
Input: 123
Output: 6
'''

import sys

def sum_the_number_of_digit(no):
    str_no = str(no)
    cnt = 0
    #print(str_no)
    for i in str_no:
        #print(i)
        cnt = cnt + int(i)
    return cnt
if __name__ == "__main__":
    args = sys.argv
    try:
        cnt = sum_the_number_of_digit(int(args[1]))
        print(cnt)
    except Exception as e:
        print("Pass the valid number for count number of digit") 