
def perform_operation(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero is not allowed."
    else:
        return "Error: Invalid operation."

num1 = float(input("Enter the first number: "))
operation = input("Enter the operation (+, -, *, /): ")
num2 = float(input("Enter the second number: "))



result = perform_operation(num1, num2, operation)


print(f"Result: {result}")
