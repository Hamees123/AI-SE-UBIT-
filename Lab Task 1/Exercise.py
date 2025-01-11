# Basic Calculator

print("Welcome to the Basic Calculator")

# Function to perform addition
def add(a, b):
    return a + b

# Function to perform subtraction
def subtract(a, b):
    return a - b

# Function to perform multiplication
def multiply(a, b):
    return a * b

# Function to perform division
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Error! Division by zero is not allowed."

# Main program loop
while True:
    print("\nOptions: add, subtract, multiply, divide, exit")
    choice = input("Enter your choice: ").lower()

    if choice in ["add", "subtract", "multiply", "divide"]:
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if choice == "add":
                result = add(num1, num2)
                print(f"Result: {num1} + {num2} = {result}")
            elif choice == "subtract":
                result = subtract(num1, num2)
                print(f"Result: {num1} - {num2} = {result}")
            elif choice == "multiply":
                result = multiply(num1, num2)
                print(f"Result: {num1} * {num2} = {result}")
            elif choice == "divide":
                result = divide(num1, num2)
                print(f"Result: {num1} / {num2} = {result}")
        except ValueError:
            print("Invalid input! Please enter numeric values.")
    elif choice == "exit":
        print("Exiting Basic Calculator. Goodbye!")
        break
    else:
        print("Invalid option. Try again.")
