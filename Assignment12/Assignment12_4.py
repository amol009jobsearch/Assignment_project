'''
4. Write a program which accepts one number and prints that many numbers starting
from 1.
'''
def main(no1):
    print(f"No1 : {no1}")
    ss=''
    for i in range(1,no1+1,1):
        ss=ss+" "+str(i)
    return ss    

if __name__ == "__main__":
    no1 = int(input("Enter Number1: "))
    result =  main(no1)
    print(f"number : {result}")