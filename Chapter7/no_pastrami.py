# List of sandwich orders with pastrami included multiple times
sandwich_orders = ['pastrami', 'tuna', 'pastrami', 'ham', 'pastrami', 'veggie']

# Print the message about running out of pastrami
print("Sorry, the deli has run out of pastrami.")

# Remove all instances of 'pastrami'
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

# Empty list for finished sandwiches
finished_sandwiches = []

# Loop through the remaining sandwich orders
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

# After all sandwiches are made
print("\nThe following sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(sandwich)
