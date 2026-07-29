'''
5.Write a program which accepts one number and prints all odd numbers till that number.
'''
import sys

def print_odd_no_till_the_no(no):
    result = []
    for i in range(1,no+1,1):
        if i % 2 == 1:
            result.append(i)
        i = i+1
    print(result)    


if __name__ == "__main__":
    args = sys.argv
    try:
        print_odd_no_till_the_no(int(args[1]))
        #print(result)
    except Exception as e:
        print("Pass the valid number for table prepareration") 