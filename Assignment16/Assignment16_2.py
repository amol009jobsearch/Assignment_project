'''
2. Write a program which contains one function named as ChkNum() which accept one
parameter as number. If number is even then it should display “Even number” otherwise
display “Odd number” on console.
Input : 11 Output : Odd Number
Input : 8 Output : Even Number
'''

def ChkNum(No1):
    if(No1%2 == 0):
        print("Even number")
    else:
        print("Odd number")    

#ChkNum(8)
ChkNum(11)