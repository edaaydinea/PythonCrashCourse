# Create dictionaries for three people
person_1 = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 28,
    'city': 'New York'
}

person_2 = {
    'first_name': 'Jane',
    'last_name': 'Smith',
    'age': 34,
    'city': 'Los Angeles'
}

person_3 = {
    'first_name': 'Mike',
    'last_name': 'Johnson',
    'age': 40,
    'city': 'Chicago'
}

# Store the dictionaries in a list
people = [person_1, person_2, person_3]

# Loop through the list and print information about each person
for person in people:
    full_name = f"{person['first_name']} {person['last_name']}"
    age = person['age']
    city = person['city']
    print(f"{full_name}, age {age}, lives in {city}.")
