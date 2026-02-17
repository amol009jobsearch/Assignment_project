'''
1. Write a program which accepts one number and prints multiplication table of that
number.
Input: 4
Output:
4 8 12 16 20 24 28 32 36 40
'''
import sys

def table_prepare(no):
    lst = []
    for i in range(1,11,1):
        #print(i*no)
        lst.append(i*no)
        i = i+1
    print(lst)    


if __name__ == "__main__":
    args = sys.argv
    try:
        table_prepare(int(args[1]))
        #print(result)
    except Exception as e:
        print("Pass the valid number for table prepareration") 