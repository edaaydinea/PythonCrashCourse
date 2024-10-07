while True:
    try:
        num1 = input("Enter the first number (or type 'quit' to exit): ")
        if num1.lower() == 'quit':
            break
        
        num2 = input("Enter the second number (or type 'quit' to exit): ")
        if num2.lower() == 'quit':
            break
        
        result = int(num1) + int(num2)
        print(f"The result is: {result}\n")
        
    except ValueError:
        print("Error: Please enter valid numbers.\n")
