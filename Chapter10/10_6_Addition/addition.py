try:
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    
    result = int(num1) + int(num2)
    print(f"The result is: {result}")
    
except ValueError:
    print("Error: Please enter valid numbers.")
