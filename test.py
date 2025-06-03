# dummy_project.py

def greet_user(name):
    print(f"Hello, {name}! This is a dummy GitHub project.")

def add(a, b):
    return a + b

def main():
    print("Welcome to the Dummy Project!")
    name = input("Enter your name: ")
    greet_user(name)

    print("\nLet's do a simple addition.")
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))
        result = add(num1, num2)
        print(f"The result of {num1} + {num2} is {result}")
    except ValueError:
        print("Please enter valid numbers.")

if __name__ == "__main__":
    main()
