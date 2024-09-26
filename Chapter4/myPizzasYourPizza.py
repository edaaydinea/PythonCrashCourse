# Original pizza list
pizzas = ['pepperoni', 'margherita', 'bbq chicken']

# Copying the list
friend_pizzas = pizzas[:]

# Adding new pizzas to each list
pizzas.append('hawaiian')
friend_pizzas.append('veggie')

# Proving the lists are separate
print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("\nMy friend’s favorite pizzas are:")
for pizza in friend_pizzas:
    print(pizza)
