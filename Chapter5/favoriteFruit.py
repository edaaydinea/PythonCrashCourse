favorite_fruits = ["apple", "banana", "orange"]

fruit = input("Enter a fruit: ")

if fruit in favorite_fruits:
    print("You really like " + fruit + "!")
else:
    print("You don't really like " + fruit + ".")