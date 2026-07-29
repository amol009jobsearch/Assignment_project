'''
4. Write a program which accepts one number and prints binary equivalent.
'''

def calculate_binary_of_number(no1):
    if no1==0:
        return "0"
    binary_nu=""

    while(no1>0):
        remainder = no1 %2
        binary_nu = str(remainder) + binary_nu
        no1 = no1//2
    return binary_nu     
             

if __name__ == "__main__":
    No1 = int(input("Enter Number: "))
    direct_fun_binary = bin(No1)
    result = calculate_binary_of_number(No1)
    print(f"{No1}'s binary equivalent : {result} : {direct_fun_binary}")
       