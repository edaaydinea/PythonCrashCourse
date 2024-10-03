# Looping Through All Values in a Dictionary
print("Looping Through All Values in a Dictionary")
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " + language.title() + ".")

# Looping Through All Keys in a Dictionary
print("\nLooping Through All Keys in a Dictionary")

for name in favorite_languages.keys():
    print(name.title())

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in friends:
        print(" Hi " + name.title() + ", I see your favorite language is " + favorite_languages[name].title() + "!")

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

# Looping Through A Dictionary's Keys in a Particular Order
print("\nLooping Through A Dictionary's Keys in a Particular Order")

for name in sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll.")

# Looping Through All Values in a Dictionary
print("\nLooping Through All Values in a Dictionary")
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())
