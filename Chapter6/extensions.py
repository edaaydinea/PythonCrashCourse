# Extended cities dictionary with a continent key
cities = {
    'New York': {
        'country': 'USA',
        'population': 8419600,
        'fact': 'Known as the Big Apple.',
        'continent': 'North America'
    },
    'London': {
        'country': 'UK',
        'population': 8982000,
        'fact': 'Home to the British monarchy.',
        'continent': 'Europe'
    },
    'Tokyo': {
        'country': 'Japan',
        'population': 13929286,
        'fact': 'Largest city in the world by population.',
        'continent': 'Asia'
    }
}

# Loop through and print information with improved formatting
for city, info in cities.items():
    print(f"\n{city}:")
    print(f"  Country: {info['country']}")
    print(f"  Population: {info['population']:,}")  # Format population with commas
    print(f"  Continent: {info['continent']}")
    print(f"  Fact: {info['fact']}")
