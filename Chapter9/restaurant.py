class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant_name and cuisine_type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        """Print the restaurant's name and cuisine type."""
        print(f"The restaurant {self.restaurant_name} serves {self.cuisine_type}.")
    
    def open_restaurant(self):
        """Print a message indicating the restaurant is open."""
        print(f"The restaurant {self.restaurant_name} is now open!")

# Create an instance of Restaurant
restaurant = Restaurant('Olive Garden', 'Italian')

# Print the two attributes
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

# Call both methods
restaurant.describe_restaurant()
restaurant.open_restaurant()
