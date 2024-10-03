# Ask the user for a number
number = int(input("Please enter a number: "))

# Check if the number is a multiple of 10
if number % 10 == 0:
    print(f"The number {number} is a multiple of 10.")
else:
    print(f"The number {number} is not a multiple of 10.")
