import json

filename = './Chapter10/numbers.json'

try:
    with open(filename) as file:
        numbers = json.load(file)
        print(numbers)
except FileNotFoundError:
    print(f"Sorry, the file {filename} was not found.")