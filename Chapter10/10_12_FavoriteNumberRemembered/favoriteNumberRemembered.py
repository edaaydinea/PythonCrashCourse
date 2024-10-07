import json

filename = './Chapter10/10_11_FavoriteNumber/favoriteNumber.json'

def get_stored_number():
    """Get stored favorite number if available."""
    try:
        with open(filename) as file:
            return json.load(file)
    except FileNotFoundError:
        return None

def get_new_number():
    """Prompt for a new favorite number."""
    favorite_number = input("What's your favorite number? ")
    with open(filename, 'w') as file:
        json.dump(favorite_number, file)
    return favorite_number

def favorite_number_program():
    favorite_number = get_stored_number()
    if favorite_number:
        print(f"I know your favorite number! It's {favorite_number}.")
    else:
        favorite_number = get_new_number()
        print(f"We'll remember your favorite number, {favorite_number}.")

favorite_number_program()
