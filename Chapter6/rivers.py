# Step 1: Create a dictionary with rivers and countries
rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'yangtze': 'china'
}

# Step 2: Loop to print a sentence about each river
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

print("\n--- Rivers ---")
# Step 3: Loop to print the name of each river
for river in rivers.keys():
    print(river.title())

print("\n--- Countries ---")
# Step 4: Loop to print the name of each country
for country in rivers.values():
    print(country.title())
