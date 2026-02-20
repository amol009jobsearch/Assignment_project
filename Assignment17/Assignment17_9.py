'''
9. Write a program which accept number from user and return number of digits in that number.
Input : 5187934 Output : 7
'''

def count_numbers(no1):
   cnt=0
   start_no1=str(no1)
   return len(start_no1)

no1 = int(input("Enter No1: "))
print(count_numbers(no1)) 