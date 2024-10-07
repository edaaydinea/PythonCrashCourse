# Handling the ZeroDivisionError Exception
print("Handling the ZeroDivisionError Exception")

try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")
    
    
# Using Exceptions to Prevent Crashes
print("\nUsing Exceptions to Prevent Crashes")

print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

while True:
    first_number = input("\nFirst number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by zero!")
    else:
        print(answer)