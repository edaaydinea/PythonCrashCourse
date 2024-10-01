current_users = ['admin', 'Jaden', 'Emily', 'Michael', 'Sarah']
new_users = ['john', 'JADEN', 'emily', 'Chris', 'Anna']

# Convert all current usernames to lowercase for case insensitive comparison
current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"The username '{new_user}' is already taken. Please enter a new username.")
    else:
        print(f"The username '{new_user}' is available.")