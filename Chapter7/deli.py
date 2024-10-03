# List of sandwich orders
sandwich_orders = ['tuna', 'ham', 'turkey', 'veggie', 'chicken']

# Empty list for finished sandwiches
finished_sandwiches = []

# Loop through the sandwich orders
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I made your {current_sandwich} sandwich.")

    # Add the finished sandwich to the finished list
    finished_sandwiches.append(current_sandwich)

# After all sandwiches are made
print("\nThe following sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(sandwich)
