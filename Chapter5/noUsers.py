usernames = ['admin', 'Jaden', 'Emily', 'Michael', 'Sarah']

# Remove all usernames
usernames.clear()

if not usernames:
    print("We need to find some users!")
else:
    for user in usernames:
        if user == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {user}, thank you for logging in again.")