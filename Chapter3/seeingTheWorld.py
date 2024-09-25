# List of places I'd like to visit
places = ['Kyoto', 'Iceland', 'New Zealand', 'Machu Picchu', 'Santorini']

# Printing the original list
print("Original list:")
print(places)

# Printing the list in alphabetical order without modifying the original list
print("\nList in alphabetical order:")
print(sorted(places))

# Showing the list is still in its original order
print("\nList after sorted() - original order retained:")
print(places)

# Printing the list in reverse alphabetical order without modifying the original list
print("\nList in reverse alphabetical order:")
print(sorted(places, reverse=True))

# Showing the list is still in its original order
print("\nList after reverse alphabetical sorted() - original order retained:")
print(places)

# Reversing the order of the list
places.reverse()
print("\nList after using reverse():")
print(places)

# Reversing the order of the list again
places.reverse()
print("\nList after reversing it back:")
print(places)

# Sorting the list in alphabetical order and modifying the original list
places.sort()
print("\nList after sort() - alphabetical order:")
print(places)

# Sorting the list in reverse alphabetical order and modifying the original list
places.sort(reverse=True)
print("\nList after sort(reverse=True) - reverse alphabetical order:")
print(places)
