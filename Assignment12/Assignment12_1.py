'''
1. Write a program which accepts one character and checks whether it is vowel or
consonant.
Input: a
Output: Vowel
'''

def main(str):
    print(f"String: {str}")
    is_vovel=False
    if str.lower() in ['a','e','i','o','u']:
        is_vovel=True
    return is_vovel
if __name__ == "__main__":
    str = input("Enter single character: ")
    result = main(str)
    if result:
        print(f"Character: {str} is vovel")
    else:
        print("Not vovel")    
