def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

def modulus(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x % y

while True:
    x = int(input("Enter the first number: "))

    operation = input("Enter the operation (+, -, *, /, %, or 'exit' to quit): ")
    if operation.lower() == "exit":
        print("Exiting calculator.")
        break
    
    y = int(input("Enter the second number: "))

    if operation == "+":
        result = add(x, y)
    elif operation == "-":
        result = subtract(x, y)
    elif operation == "*":
        result = multiply(x, y)
    elif operation == "/":
        result = divide(x, y)
    elif operation == "%":
        result = modulus(x, y)
    else:
        result = "Error: Invalid operation"

    print("Result:", result)