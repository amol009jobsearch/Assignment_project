'''
7. Write a program which accept one number and display below pattern.
Input : 5
Output : 
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
'''

def display_pattern(no1):
   #star=""
   for i in range(1,no1+1,1):
        star=""
        for j in range (1,no1+1,1):
            star = star + str(j) + " "      
        print(star)

no1 = int(input("Enter No1: "))
display_pattern(no1)