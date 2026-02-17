'''
4. Write a program which accepts one number and prints cube of that number.
'''
import sys

def no_divisible_by_3_or_5(no):
    if no%3 == 0 and no%5 == 0:
        print(f"No: {no} is divisible by 3 and 5")
    else:
        print("Not divisible by 3 and 5")        


if __name__ == "__main__":
    args = sys.argv
    try:
        no_divisible_by_3_or_5(float(args[1]))
        #print(result)
    except Exception as e:
        print("Pass the valid number for division")    