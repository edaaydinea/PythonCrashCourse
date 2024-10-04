class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant_name, cuisine_type, and number_served attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0  # Default value of 0
    
    def describe_restaurant(self):
        """Print the restaurant's name and cuisine type."""
        print(f"The restaurant {self.restaurant_name} serves {self.cuisine_type}.")
    
    def open_restaurant(self):
        """Print a message indicating the restaurant is open."""
        print(f"The restaurant {self.restaurant_name} is now open!")
    
    def set_number_served(self, number):
        """Set the number of customers served."""
        self.number_served = number
    
    def increment_number_served(self, additional_customers):
        """Increment the number of customers served by a certain number."""
        self.number_served += additional_customers

# Create an instance of Restaurant
restaurant = Restaurant('Olive Garden', 'Italian')

# Print the default number of customers served
print(f"Customers served: {restaurant.number_served}")

# Change the number of customers served and print it again
restaurant.number_served = 5
print(f"Customers served: {restaurant.number_served}")

# Use set_number_served method and print the value
restaurant.set_number_served(20)
print(f"Customers served: {restaurant.number_served}")

# Increment the number of customers served and print the value
restaurant.increment_number_served(30)
print(f"Customers served: {restaurant.number_served}")
