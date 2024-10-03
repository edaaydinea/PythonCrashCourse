# Dictionary to store vacation choices
dream_vacations = {}

# Polling loop
polling_active = True

while polling_active:
    # Ask user for their name and dream vacation
    name = input("What's your name? ")
    vacation = input("If you could visit one place in the world, where would you go? ")

    # Store the response
    dream_vacations[name] = vacation

    # Ask if they want to let someone else respond
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat.lower() == 'no':
        polling_active = False

# Poll results
print("\n--- Dream Vacation Poll Results ---")
for name, vacation in dream_vacations.items():
    print(f"{name} would like to visit {vacation}.")
