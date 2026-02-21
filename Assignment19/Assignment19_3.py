'''
3.Write a program which contains filter(), map() and reduce() in it. Python application which
contains one list of numbers. List contains the numbers which are accepted from user. Filter
should filter out all such numbers which greater than or equal to 70 and less than or equal to
90. Map function will increase each number by 10. Reduce will return product of all that
numbers.
Input List = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
List after filter = [76, 89, 86, 90, 70]
List after map = [86, 99, 96, 100, 80]
Output of reduce = 6538752000
'''
from functools import reduce
from Custom_Module.Arithmetic import lambda_filter,lambda_map,lambda_reduce

def main():
    try:
        Border = "*"*30
        no_of_elements_in_list = int(input("Enter how many elements you want in list?  :"))
        if no_of_elements_in_list:
            num_list=[]
            for i in range(1,no_of_elements_in_list+1,1):
                element=int(input("Enter element to add in list: "))
                num_list.append(element)
            print("Final list : {}".format(num_list))
            print(Border)
            filter_data = list(filter(lambda_filter,num_list)) 
            print("filter_data : {}".format(filter_data))
            print(Border)
            map_data = list(map(lambda_map,num_list))
            print("map_data : {}".format(map_data))
            print(Border)
            reduce_data = reduce(lambda_reduce,num_list)
            print("reduce_data : {}".format(reduce_data))

    except Exception as e:
        print("Exception in code : {}".format(e))

if __name__ == "__main__":
    main()