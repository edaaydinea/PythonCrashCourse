# List of guests
guests = ['Nikola Tesla', 'Isaac Newton', 'Charles Darwin', 'Marie Curie', 'Ada Lovelace', 'Rosalind Franklin']

# Informing that only two guests can be invited
print("\nSorry, the new table won't arrive on time, and I can only invite two people for dinner.\n")

# Removing guests until only two remain
while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Sorry {removed_guest}, I can't invite you to dinner.")

# Messages to the remaining two guests
for guest in guests:
    print(f"Dear {guest}, you're still invited to dinner!")

# Deleting the last two guests
del guests[0]
del guests[0]

# Printing the empty list
print(f"\nFinal guest list: {guests}")
