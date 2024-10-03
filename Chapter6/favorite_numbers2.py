# Create a dictionary of favorite numbers
favorite_numbers = {
    'John': [7, 14, 21],
    'Jane': [3, 8],
    'Mike': [42, 16]
}

# Loop through and print each person's favorite numbers
for person, numbers in favorite_numbers.items():
    print(f"{person}'s favorite numbers are:")
    for number in numbers:
        print(f"- {number}")
    print()
