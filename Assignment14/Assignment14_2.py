'''
2. Write a lambda function which accepts one number and returns cube of that number.
'''
#normal function to calculate cube
def calculate_cube(no1):
    return no1*no1*no1

#lambda function to calculate cube
cube_of_number = lambda no1 : no1*no1*no1

if __name__ == "__main__":
    print("")
    no1 = int(input("Enter Number: "))
    res_manual = calculate_cube(no1)
    print(f"res_manual: {res_manual}")
    print(f"res_lambda: {cube_of_number(no1)}")
