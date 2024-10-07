import json

filename = './Chapter10/10_13_VerifyUser/username.json'

def get_stored_username():
    """Get stored username if available."""
    try:
        with open(filename) as file:
            return json.load(file)
    except FileNotFoundError:
        return None

def get_new_username():
    """Prompt for a new username."""
    username = input("What's your name? ")
    with open(filename, 'w') as file:
        json.dump(username, file)
    return username

def greet_user():
    """Greet the user by name, with verification."""
    username = get_stored_username()
    if username:
        correct_user = input(f"Are you {username}? (yes/no) ")
        if correct_user.lower() == 'yes':
            print(f"Welcome back, {username}!")
        else:
            username = get_new_username()
            print(f"We'll remember you when you come back, {username}.")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}.")

greet_user()
