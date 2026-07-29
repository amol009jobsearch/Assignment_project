'''
4.Write a program which contains filter(), map() and reduce() in it. Python application which
contains one list of numbers. List contains the numbers which are accepted from user. Filter
should filter out all such numbers which are even. Map function will calculate its square.
Reduce will return addition of all that numbers.
Input List = [5, 2, 3, 4, 3, 4, 1, 2, 8, 10]
List after filter = [2, 4, 4, 2, 8, 10]
List after map = [4, 16, 16, 4, 64, 100]
Output of reduce = 204
'''
from functools import reduce
lambda_filter_even_number = lambda x : x%2 == 0
lambda_map_square_of_element = lambda x : x*x
lambda_reduce_addition = lambda x,y : x+y

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
            filter_data = list(filter(lambda_filter_even_number,num_list)) 
            print("filter_data : {}".format(filter_data))
            print(Border)
            map_data = list(map(lambda_map_square_of_element,num_list))
            print("map_data : {}".format(map_data))
            print(Border)
            reduce_data = reduce(lambda_reduce_addition,num_list)
            print("reduce_data : {}".format(reduce_data))

    except Exception as e:
        print("Exception in code : {}".format(e))

if __name__ == "__main__":
    main()