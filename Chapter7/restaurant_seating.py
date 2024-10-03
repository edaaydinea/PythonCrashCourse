# Ask the user how many people are in their dinner group
group_size = int(input("How many people are in your dinner group? "))

# Check if the group size is more than 8
if group_size > 8:
    print("You’ll have to wait for a table.")
else:
    print("Your table is ready!")
