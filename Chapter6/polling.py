# The favorite_languages dictionary from favorite_languages.py
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

# Step 1: Create a list of people who should take the poll
people_to_poll = ['jen', 'sarah', 'edward', 'phil', 'mike', 'linda']

# Step 2: Loop through the list of people and check if they have taken the poll
for person in people_to_poll:
    if person in favorite_languages:
        print(f"Thank you, {person.title()}, for taking the poll!")
    else:
        print(f"{person.title()}, please take the favorite languages poll!")
