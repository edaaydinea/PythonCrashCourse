# List of programming languages
languages = ['Python', 'JavaScript', 'C++', 'Go', 'Rust']

# Printing the original list
print("Original list of languages:")
print(languages)

# Using sorted() to display the list in alphabetical order without modifying the original
print("\nLanguages in alphabetical order:")
print(sorted(languages))

# Showing the original list is unchanged
print("\nOriginal list after using sorted():")
print(languages)

# Using sorted() to display the list in reverse alphabetical order without modifying the original
print("\nLanguages in reverse alphabetical order:")
print(sorted(languages, reverse=True))

# Showing the original list is unchanged
print("\nOriginal list after using reverse sorted():")
print(languages)

# Using reverse() to change the order of the list
languages.reverse()
print("\nList after using reverse():")
print(languages)

# Reversing the order back
languages.reverse()
print("\nList after using reverse() again:")
print(languages)

# Sorting the list in alphabetical order permanently
languages.sort()
print("\nList after using sort() - alphabetical order:")
print(languages)

# Sorting the list in reverse alphabetical order permanently
languages.sort(reverse=True)
print("\nList after using sort(reverse=True) - reverse alphabetical order:")
print(languages)

# Using len() to find out the number of items in the list
print(f"\nThere are {len(languages)} programming languages in the list.")

# Using append() to add an item to the list
languages.append('Swift')
print("\nList after appending 'Swift':")
print(languages)

# Using insert() to add an item at a specific position
languages.insert(2, 'Kotlin')
print("\nList after inserting 'Kotlin' at position 2:")
print(languages)

# Using pop() to remove the last item from the list
popped_language = languages.pop()
print(f"\nList after using pop(): {languages}")
print(f"Popped language: {popped_language}")

# Using del to remove an item by index
del languages[1]
print("\nList after deleting the second language:")
print(languages)

# Using remove() to delete an item by value
languages.remove('Go')
print("\nList after removing 'Go':")
print(languages)
