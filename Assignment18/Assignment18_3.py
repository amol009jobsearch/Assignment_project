'''
3.Write a program which accept N numbers from user and store it into List. Return Minimum
number from that List.
Input : Number of elements : 4
Input Elements : 13 5 45 7
Output : 5
'''

def min_from_list(No1):
    num_list=[]
    sum=0
    for i in range(1,No1+1,1):
        val = int(input("Enter Element to add in list: "))
        num_list.append(val)
    #13 5 45 7    
    print(f"Elements of list : {num_list}")    
    min = num_list[0]
    for val in num_list:
        if val < min:
            min = val
    print(f"min : {min}")

No1 = int(input("Enter list size: "))
min_from_list(No1)