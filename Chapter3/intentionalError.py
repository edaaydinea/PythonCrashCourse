# List of programming languages
languages = ['Python', 'JavaScript', 'C++', 'Go', 'Rust']

# Intentionally causing an IndexError by trying to access an index that doesn't exist
print("\nTrying to access an invalid index:")
print(languages[5])  # This will cause an IndexError because the list has only 5 elements (index 0 to 4)


"""
# List of programming languages
languages = ['Python', 'JavaScript', 'C++', 'Go', 'Rust']

# Correctly accessing an existing index
print("\nAccessing a valid index:")
print(languages[4])  # This will print 'Rust' because it's at index 4, the last valid index
"""