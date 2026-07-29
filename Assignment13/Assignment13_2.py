'''
2. Write a program which accepts radius of circle and prints area of circle.
'''

def calculate_area_of_circle(radius):
    if radius:
        return (22*radius*radius)/7
    else:
        print("either radius is none or zero")

if __name__ == "__main__":
    radius = float(input("Enter Radius: "))
    area = calculate_area_of_circle(radius)
    print(f"Area of circle is : {area}")