# Create dictionaries for different pets
pet_1 = {'kind': 'dog', 'owner': 'Alice'}
pet_2 = {'kind': 'cat', 'owner': 'Bob'}
pet_3 = {'kind': 'parrot', 'owner': 'Charlie'}

# Store the dictionaries in a list
pets = [pet_1, pet_2, pet_3]

# Loop through the list and print information about each pet
for pet in pets:
    kind = pet['kind']
    owner = pet['owner']
    print(f"{owner} owns a {kind}.")
