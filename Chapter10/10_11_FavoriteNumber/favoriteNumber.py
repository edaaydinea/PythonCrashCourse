import json

filename = './Chapter10/10_11_FavoriteNumber/favoriteNumber.json'

try:
    with open(filename) as file:
        favorite_number = json.load(file)
        print(f"I know your favorite number! It's {favorite_number}.")
except FileNotFoundError:
    favorite_number = input("What is your favorite number? ")
    with open(filename, 'w') as file:
        json.dump(favorite_number, file)
        print("I'll remember your favorite number.")
        
# Output:
# What is your favorite number? 7
# I'll remember your favorite number.

