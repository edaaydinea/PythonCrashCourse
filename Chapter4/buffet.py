# Original buffet menu stored in a tuple
buffet_menu = ('pizza', 'pasta', 'salad', 'soup', 'bread')

# Printing the foods in the buffet menu
print("The buffet offers the following foods:")
for food in buffet_menu:
    print(food)

# Uncommenting the following line will raise an error because tuples are immutable.
# buffet_menu[0] = 'sushi'  # This will result in a TypeError

# Updating the buffet menu by replacing two items
buffet_menu = ('pizza', 'pasta', 'sushi', 'ramen', 'bread')

# Printing the revised menu
print("\nThe revised buffet menu offers the following foods:")
for food in buffet_menu:
    print(food)
