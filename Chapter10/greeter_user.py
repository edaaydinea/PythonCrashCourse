import json

def get_stored_username():
    """Get stored username if available."""
    filename = './Chapter10/username2.json'
    
    try:
        with open(filename) as file:
            username = json.load(file)
    except FileNotFoundError:
        return None
    else:
        return username
    
    
def get_new_username():
    """Prompt for a new username."""
    username = input("What is your name? ")
    filename = './Chapter10/username.json'
    
    with open(filename, 'w') as file:
        json.dump(username, file)
    return username
    

def greeter_user():
    """Greet the user by name."""
    username = get_stored_username()
    
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")
        
        
greeter_user()