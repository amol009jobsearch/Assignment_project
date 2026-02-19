'''
2.Write a program which accepts one number and prints count of digits in that number.
Input: 7521
Output: 4
'''

import sys

def count_the_number_of_digit(no):
    str_no = str(no)
    cnt = 0
    #print(str_no)
    for i in str_no:
        #print(i)
        cnt = cnt + 1
    return cnt
if __name__ == "__main__":
    args = sys.argv
    try:
        cnt = count_the_number_of_digit(int(args[1]))
        print(cnt)
    except Exception as e:
        print("Pass the valid number for count number of digit") 