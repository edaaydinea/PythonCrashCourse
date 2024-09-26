pizzas = ['pepperoni', 'margherita', 'bbq chicken', 'hawaiian', 'veggie']

# The first three items
print("The first three items in the list are:")
print(pizzas[:3])

# Three items from the middle
print("Three items from the middle of the list are:")
middle_index = len(pizzas) // 2
print(pizzas[middle_index - 1: middle_index + 2])

# The last three items
print("The last three items in the list are:")
print(pizzas[-3:])
