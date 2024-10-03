# Use a dictionary to store people's favorite numbers.
# Think of five names, and use them as keys in your dictionary.
# Think of a favorite number for each person, and store each as a value in your dictionary. Print each person's name and their favorite number.
# For even more fun, poll a few friends and get some actual data for your program.

favorite_numbers = {
    'john': 7,
    'jane': 3,
    'jim': 5,
    'jill': 9,
    'jack': 2,
}

# Print each person's favorite number
for name, number in favorite_numbers.items():
    print(f"{name.title()}'s favorite number is {number}.")

print("\n")

# Polling friends and adding their favorite numbers
new_favorites = {
    'sarah': 6,
    'mike': 8,
    'kate': 4,
}

favorite_numbers.update(new_favorites)

# Print each person's favorite number again
for name, number in favorite_numbers.items():
    print(f"{name.title()}'s favorite number is {number}.")

