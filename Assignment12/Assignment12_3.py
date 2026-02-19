'''
3. Write a program which accepts two numbers and prints addition, subtraction,
multiplication and division.
'''
def addition(no1,no2):
    res=0
    if no1 and no2:
        res=no1+no2
    else:
        print("either no1 or no2 is None or Zero")    
    return res    

def substraction(no1,no2):
    res=0
    if no1 and no2:
        res=no1-no2
    else:
        print("either no1 or no2 is None or Zero")    
    return res  

def multiplication(no1,no2):
    res=0
    if no1 and no2:
        res=no1*no2
    else:
        print("either no1 or no2 is None or Zero")    
    return res  

def division(no1,no2):
    res=0
    if no1 and no2:
        res=no1/no2
    else:
        print("either no1 or no2 is None or Zero")    
    return res  


def main(no1,no2):
    print(f"No1 : {no1}")
    print(f"No2 : {no2}")
    res_add = addition(no1,no2)
    print(f"addition of two number: {res_add}")

    res_sub = substraction(no1,no2)
    print(f"substraction of two number: {res_sub}")

    res_mul = multiplication(no1,no2)
    print(f"multiplication of two number: {res_mul}")

    res_div = division(no1,no2)
    print(f"division of two number: {res_div}")
    

if __name__ == "__main__":
    no1 = int(input("Enter Number1: "))
    no2 = int(input("Enter Number2: "))
    main(no1,no2)