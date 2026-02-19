'''
2. Write a program which accepts one number and prints its factors.
Input: 12
Output: 1 2 3 4 6 12
'''

def main(no):
    print(f"No : {no}")
    list_of_factors=[]
    for i in range(1,no+1,1):
        if no%i == 0:
            list_of_factors.append(i)
    return list_of_factors

if __name__ == "__main__":
    no = int(input("Enter Number: "))
    result = main(no)
    if result:
        print(f"Factors of number: {result}")