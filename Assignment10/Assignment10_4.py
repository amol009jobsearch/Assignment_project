'''
4. Write a program which accepts one number and prints all even numbers till that
number.
Input: 10
Output: 2 4 6 8 10
'''
import sys

def print_even_no_till_the_no(no):
    result = []
    for i in range(2,no+1,1):
        if i % 2 == 0:
            result.append(i)
        i = i+1
    print(result)    


if __name__ == "__main__":
    args = sys.argv
    try:
        print_even_no_till_the_no(int(args[1]))
        #print(result)
    except Exception as e:
        print("Pass the valid number for table prepareration") 