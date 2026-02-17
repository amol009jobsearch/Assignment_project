'''
2. Write a program which accepts one number and prints sum of first N natural numbers.
Input: 5
Output: 15
'''
import sys

def sum_of_n_natural_no(no):
    result = 1
    for i in range(2,no+1,1):
        #print(i*no)
        result = result + i
        i = i+1
    print(result)    


if __name__ == "__main__":
    args = sys.argv
    try:
        sum_of_n_natural_no(int(args[1]))
        #print(result)
    except Exception as e:
        print("Pass the valid number for table prepareration") 