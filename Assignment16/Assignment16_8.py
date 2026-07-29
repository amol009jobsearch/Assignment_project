'''
8. Write a program which accept number from user and print that number of “*” on screen.
Input : 5 Output : * * * * *
'''
def display_stars(no):
    if no:
        for i in range(1,no+1,1):
            print("*")
    else:
        print("Either no is None or Zero.. Enter Valid number")    
    

if __name__ == "__main__":
    no = int(input("Enter Number : "))
    display_stars(no)