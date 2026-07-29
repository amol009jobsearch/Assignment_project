'''
1. Write a program which accepts length and width of rectangle and prints area.
'''

def calculate_area_of_rectangle(length,width):
    if length and width:
        return length * width
    else:
        print("either width or length is none or zero")

if __name__ == "__main__":
    length = float(input("Enter Length: "))
    width = float(input("Enter Width: "))
    area = calculate_area_of_rectangle(length,width)
    print(f"Area of rectangle is : {area}")