def Add(no1,no2):
    return no1+no2

def Sub(no1,no2):
    return no1-no2

def Mult(no1,no2):
    return no1*no2

def Div(no1,no2):
    return no1/no2

def ChkPrime(No1):
    is_prime = True
    for i in range(2,No1,1):
        if No1%i == 0:
            is_prime=False
    return is_prime