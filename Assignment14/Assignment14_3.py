'''
3. Write a lambda function which accepts two numbers and returns maximum number.
'''
#normal function to calculate cube
def calculate_max(no1,no2):
    max = 0
    if no1 > no2:
        max = no1
    else:
        max = no2
    return max        

if __name__ == "__main__":
    print("")
    no1 = float(input("Enter Number1: "))
    no2 = float(input("Enter Number2: "))
    result = calculate_max(no1,no2)
    print(f"Max among {no1} and {no2} is :-> {result}")