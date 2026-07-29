'''
1.Write a program which accept N numbers from user and store it into List. Return addition of all
elements from that List.
Input : Number of elements : 6
Input Elements : 13 5 45 7 4 56
Output : 130
'''

def create_list_addition_of_elements(No1):
    num_list=[]
    sum=0
    for i in range(1,No1+1,1):
        val = int(input("Enter Element to add in list: "))
        num_list.append(val)
        sum = sum+val
    print(f"Elements of list : {num_list}")    
    print(f"Sum of Elements : {sum}")    

No1 = int(input("Enter list size: "))
create_list_addition_of_elements(No1)