def display(name: str, age: int):
    print(f"Hello {name}, you will turn {age + 1} next year.")

def prompt_name():
    name = input("Enter name: ").strip()
    if not name:
        raise ValueError("Name is required")
    return name or "User"

def prompt_age():
    s= input("Enter age: ").strip()
    if not s:
        raise ValueError("Age is required")
    age = int(s)
    if int(age) < 0:
        raise ValueError("Age cannot be negative")
    return age

def main():
    try:
        name = prompt_name()
        age = prompt_age()
        display(name, age)
    except ValueError as e:
        print(f"Input value for name or age is not entered correctly: {e}")
    except Exception as e:
        print(f"Some error occurred: {e}")

if __name__ == "__main__":
    main()