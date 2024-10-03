# Conditional test to stop the loop
topping = ""
while topping.lower() != 'quit':
    topping = input("Enter a pizza topping (type 'quit' to stop): ")

    if topping.lower() != 'quit':
        print(f"I'll add {topping} to your pizza!")


# Using an active variable to control the loop
active = True
while active:
    age = input("Enter your age (or type 'quit' to stop): ")

    if age.lower() == 'quit':
        active = False
    else:
        age = int(age)
        if age < 3:
            print("Your ticket is free!")
        elif 3 <= age <= 12:
            print("Your ticket costs $10.")
        else:
            print("Your ticket costs $15.")


# Using break to exit the loop
while True:
    topping = input("Enter a pizza topping (type 'quit' to stop): ")

    if topping.lower() == 'quit':
        break
    else:
        print(f"I'll add {topping} to your pizza!")
