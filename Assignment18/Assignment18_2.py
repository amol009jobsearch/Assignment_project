'''
2.Write a program which accept N numbers from user and store it into List. Return Maximum
number from that List.
Input : Number of elements : 7
Input Elements : 13 5 45 7 4 56 34
Output : 56
'''

def max_from_list(No1):
    num_list=[]
    sum=0
    for i in range(1,No1+1,1):
        val = int(input("Enter Element to add in list: "))
        num_list.append(val)
        
    print(f"Elements of list : {num_list}")    
    max = 0
    for val in num_list:
        if val>max:
            max = val
    print(f"max : {max}")

No1 = int(input("Enter list size: "))
max_from_list(No1)