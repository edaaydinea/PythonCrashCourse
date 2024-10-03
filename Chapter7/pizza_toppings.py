# Loop for pizza toppings
while True:
    topping = input("Enter a pizza topping (type 'quit' to stop): ")

    if topping.lower() == 'quit':
        break
    else:
        print(f"I'll add {topping} to your pizza!")
