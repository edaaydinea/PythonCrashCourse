class Restaurant:
    """A simple attempt to represent a restaurant."""
    
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize attributes to describe a restaurant."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        """Print the restaurant's name and cuisine type."""
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")
        
    def open_restaurant(self):
        """Print a message indicating that the restaurant is open."""
        print(f"{self.restaurant_name} is now open!")

class IceCreamStand(Restaurant):
    """Represent aspects of a restaurant specific to an ice cream stand."""
    
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize attributes of the parent class and an ice cream stand."""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []  # Initialize an empty list of flavors
        
    def add_flavor(self, flavor):
        """Add a new flavor to the list of flavors."""
        self.flavors.append(flavor)
        
    def display_flavors(self):
        """Display the available ice cream flavors."""
        print("Available ice cream flavors:")
        for flavor in self.flavors:
            print(f"- {flavor}")

# Create an instance of IceCreamStand
my_stand = IceCreamStand("Sweet Treats", "Dessert")
my_stand.add_flavor("Chocolate")
my_stand.add_flavor("Vanilla")
my_stand.add_flavor("Strawberry")

# Call methods
my_stand.describe_restaurant()
my_stand.display_flavors()
my_stand.open_restaurant()
