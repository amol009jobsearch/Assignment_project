'''
4.Write a program which accept N numbers from user and store it into List. Accept one another
number from user and return frequency of that number from List.
Input : Number of elements : 11
Input Elements : 13 5 45 7 4 56 5 34 2 5 65
Element to search : 5
Output : 3
'''

def frequence_of_number(No1):
    num_list=[]
    sum=0
    for i in range(1,No1+1,1):
        val = int(input("Enter Element to add in list: "))
        num_list.append(val)
    #13 5 45 7    
    print(f"Elements of list : {num_list}")
    search_element = int(input("Enter Element to search:"))
    
    count = 0
    for val in num_list:
        if val == search_element:
            count = count + 1
    print(f"frequency of {search_element} is : {count}")

No1 = int(input("Enter list size: "))
frequence_of_number(No1)