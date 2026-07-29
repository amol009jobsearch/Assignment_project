'''
6. Write a program which accept one number and display below pattern.
Input : 5
Output : 
* * * * *
* * * *
* * *
* *
*
'''
import copy
def reverse_triangle(no1):
    no2=copy.copy(no1)
    #star=""
    for i in range(1,no1+1,1):
        #print(i * "*")
        star =""
        for j in range(1,no2+1,1):
            star = star + "* "
        print(star)    
        no2 = no2 - 1
        
     
no1 = int(input("Enter No1: "))
reverse_triangle(no1)