# Create a dictionary of cities
cities = {
    'New York': {
        'country': 'USA',
        'population': 8419600,
        'fact': 'Known as the Big Apple.'
    },
    'London': {
        'country': 'UK',
        'population': 8982000,
        'fact': 'Home to the British monarchy.'
    },
    'Tokyo': {
        'country': 'Japan',
        'population': 13929286,
        'fact': 'Largest city in the world by population.'
    }
}

# Loop through the cities dictionary and print information about each city
for city, info in cities.items():
    print(f"{city}:")
    print(f"  Country: {info['country']}")
    print(f"  Population: {info['population']}")
    print(f"  Fact: {info['fact']}\n")
