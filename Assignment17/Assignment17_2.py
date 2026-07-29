'''
2. Write a program which accept one number and display below pattern.
Input : 5
Output : 
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
'''

def display_stars(no1):
    for i in range(1,no1+1,1):
        str = ""
        for j in range(1,no1+1,1):
            str = str + "* "
        print(str)

no1 = int(input("Enter No1: "))
display_stars(no1)