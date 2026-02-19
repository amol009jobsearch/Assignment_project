'''
4. Write a lambda function which accepts two numbers and returns minimum number.'''
#normal function to calculate cube
def calculate_min(no1,no2):
    min = 0
    if no1 > no2:
        min = no2
    else:
        min = no1
    return min        

if __name__ == "__main__":
    print("")
    no1 = float(input("Enter Number1: "))
    no2 = float(input("Enter Number2: "))
    result = calculate_min(no1,no2)
    print(f"Min among {no1} and {no2} is :-> {result}")