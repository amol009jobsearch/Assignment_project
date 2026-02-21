'''
5.Write a program which accept N numbers from user and store it into List. Return addition of all
prime numbers from that List. Main python file accepts N numbers from user and pass each
number to ChkPrime() function which is part of our user defined module named as
MarvellousNum. Name of the function from main python file should be ListPrime().
Input : Number of elements : 11
Input Elements : 13 5 45 7 4 56 10 34 2 5 8
Output : 54 (13 + 5 + 7 +2 + 5)
'''

from Assignment17.Arithmetic import ChkPrime        

def add_elements_in_list(No1):
    num_list=[]
    for i in range(1,No1+1,1):
        val = int(input("Enter Element to add in list: "))
        num_list.append(val)
    #13 5 45 7    
    print(f"Elements of list : {num_list}")
    sum=0
    for no in num_list:
        is_prime = ChkPrime(no)
        if is_prime:
            print(f"prime number : {no}")
            sum = sum + no
    print(f"sum of prime number: {sum}")
if __name__ == "__main__":
    No1 = int(input("Enter list size: "))
    add_elements_in_list(No1)   
 