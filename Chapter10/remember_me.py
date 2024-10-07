import json

username = input("What is your name? ")

filename = './Chapter10/username.json'

with open(filename, 'w') as file:
    json.dump(username, file)
    print(f"We'll remember you when you come back, {username}!")