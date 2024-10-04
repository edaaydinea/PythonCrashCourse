class User:
    """A simple attempt to represent a user profile."""
    
    def __init__(self, first_name, last_name):
        """Initialize attributes to describe a user."""
        self.first_name = first_name
        self.last_name = last_name
        
    def describe_user(self):
        """Print a summary of the user's information."""
        print(f"User: {self.first_name} {self.last_name}")
        
    def greet_user(self):
        """Print a personalized greeting to the user."""
        print(f"Hello, {self.first_name}!")

class Admin(User):
    """Represent aspects of a user specific to an administrator."""
    
    def __init__(self, first_name, last_name):
        """Initialize attributes of the parent class and admin."""
        super().__init__(first_name, last_name)
        self.privileges = ["can add post", "can delete post", "can ban user"]
        
    def show_privileges(self):
        """Print a list of administrator privileges."""
        print(f"Administrator Privileges: {', '.join(self.privileges)}")

# Create an instance of Admin
admin_user = Admin("Alice", "Smith")
admin_user.describe_user()
admin_user.show_privileges()
