'''
5. Write a program which accepts marks and displays grade.
Condition Example:
• ≥ 75 → Distinction
• ≥ 60 → First Class
• ≥ 50 → Second Class
• < 50 → Fail
'''

def displays_grade(no1):
    if no1:
        if no1>=75:
            print("Distinction")
        elif no1>=60 < 75:
            print("First Class")
        elif no1>=50 < 60:
            print("Second Class")   
        else:
            print("Fail")            
    else:
        print("either percentage is none or zero")     
             

if __name__ == "__main__":
    try:
        marks = float(input("Enter percentage: "))
        displays_grade(marks)
    except Exception as e:
        print("Enter valid percentage: {}".format(e))
       