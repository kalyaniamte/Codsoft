def calculator():
    # Prompt the user to input two numbers
    num_1 = float(input("Enter the first number: "))
    num_2 = float(input("Enter the second number: "))
    
    # Prompt the user to choose an operation
    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    operation = input("Enter the operation (1/2/3/4): ")
    
    # Perform the calculation based on the chosen operation
    if operation == '1':
        result = num_1 + num_2
        operation_symbol = "+"
    elif operation == '2':
        result = num_1 - num_2
        operation_symbol = "-"
    elif operation == '3':
        result = num_1 * num_2
        operation_symbol = "*"
    elif operation == '4':
        if num_2 != 0:
            result = num_1 / num_2
            operation_symbol = "/"
        else:
            return "Error! Division by zero is not allowed."
    else:
        return "Invalid operation. Please choose 1, 2, 3, or 4."
    
    # Display the result
    return f"The result of {num_1} {operation_symbol} {num_2} is: {result}"

# Call the calculator function
print(calculator())