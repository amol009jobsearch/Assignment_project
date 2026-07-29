'''
10. Write a program which accept number from user and return addition of digits in that number.
Input : 5187934 Output : 37
'''

def cal_Add(start):
    sum=0
    for i in range(1,len(start)+1,1):
        sum = sum+int(i)
    print(sum)    
start = input("Enter number")
cal_Add(start)
