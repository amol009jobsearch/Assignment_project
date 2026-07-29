'''
5.Write a program which contains filter(), map() and reduce() in it. Python application which
contains one list of numbers. List contains the numbers which are accepted from user. Filter
should filter out all prime numbers. Map function will multiply each number by 2. Reduce will
return Maximum number from that numbers. (You can also use normal functions instead of
lambda functions).
Input List = [2, 70 , 11, 10, 17, 23, 31, 77]
List after filter = [2, 11, 17, 23, 31]
List after map = [4, 22, 34, 46, 62]
Output of reduce = 62
'''
from functools import reduce
is_prime = lambda n: n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))
lambda_map_square_of_element = lambda x : x*2
max_value = lambda v1, v2: v1 if v1 >= v2 else v2

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
            filter_data = list(filter(is_prime,num_list)) 
            print("filter_data : {}".format(filter_data))
            print(Border)
            map_data = list(map(lambda_map_square_of_element,num_list))
            print("map_data : {}".format(map_data))
            print(Border)
            reduce_data = reduce(max_value,num_list)
            print("reduce_data : {}".format(reduce_data))

    except Exception as e:
        print("Exception in code : {}".format(e))

if __name__ == "__main__":
    main()