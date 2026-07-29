'''
4. Write a program which accepts one number and prints cube of that number.
'''
import sys

def cube_of_number(no):
    return no*no*no


if __name__ == "__main__":
    args = sys.argv
    try:
        cube = cube_of_number(float(args[1]))
        print(cube)
    except Exception as e:
        print("Pass the valid number for cube")    