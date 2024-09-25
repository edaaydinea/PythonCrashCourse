# List of guests
guests = ['Isaac Newton', 'Marie Curie', 'Ada Lovelace']

# Informing about a bigger table
print("\nGood news! We found a bigger dinner table, so we're inviting more people.\n")

# Adding more guests
guests.insert(0, 'Nikola Tesla')  # Insert at the beginning
guests.insert(2, 'Charles Darwin')  # Insert in the middle
guests.append('Rosalind Franklin')  # Append to the end

# New invitations
for guest in guests:
    print(f"Dear {guest}, you are invited to dinner!")
