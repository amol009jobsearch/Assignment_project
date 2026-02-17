'''
3. Write a program which accepts one number and prints factorial of that number.
Input: 5
Output: 120
'''
import sys

def factorial_of_a_number(no):
    result = 1
    for i in range(2,no+1,1):
        #print(i*no)
        result = result * i
        i = i+1
    print(result)    


if __name__ == "__main__":
    args = sys.argv
    try:
        factorial_of_a_number(int(args[1]))
        #print(result)
    except Exception as e:
        print("Pass the valid number for table prepareration") 