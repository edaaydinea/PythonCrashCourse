# Create a dictionary of favorite places
favorite_places = {
    'John': ['Paris', 'New York', 'Rome'],
    'Jane': ['London', 'Tokyo'],
    'Mike': ['Berlin', 'Amsterdam', 'Sydney']
}

# Loop through the dictionary and print each person's favorite places
for person, places in favorite_places.items():
    print(f"{person}'s favorite places are:")
    for place in places:
        print(f"- {place}")
    print()
