# Program to get user's name and write it to guest.txt
filename = './Chapter10/10_3_Guest/guest.txt'

name = input("Please enter your name: ")

with open(filename, 'w') as file:
    file.write(name)

print(f"Hello, {name}! Your name has been written to {filename}.")
