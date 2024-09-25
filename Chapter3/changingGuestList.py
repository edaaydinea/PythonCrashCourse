# List of guests
guests = ['Albert Einstein', 'Marie Curie', 'Ada Lovelace']

# Initial invitations
for guest in guests:
    print(f"Dear {guest}, you are invited to dinner!")

# One guest can't make it
print(f"\nUnfortunately, {guests[0]} can't make it to dinner.\n")

# Replacing the guest who can't come
guests[0] = 'Isaac Newton'

# New invitations
for guest in guests:
    print(f"Dear {guest}, you are still invited to dinner!")
