'''
5. Write a program which accepts one number and prints that many numbers in reverse
order.
Input: 5
Output: 5 4 3 2 1
'''
def main(no1):
    print(f"No1 : {no1}")
    ss=''
    string_no1 = str(no1)
    itr = len(str(no1))
    while(itr>0):
        itr = itr - 1
        ss = ss + ""+string_no1[itr]
        
    return ss    
if __name__ == "__main__":
    no1 = int(input("Enter Number1: "))
    result =  main(no1)
    print(f"reverse of number {no1} is : {result}")