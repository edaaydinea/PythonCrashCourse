from admin import User


class Privileges:
    """Represent a set of privileges for an admin user."""
    
    def __init__(self):
        """Initialize privileges."""
        self.privileges = ["can add post", "can delete post", "can ban user"]
        
    def show_privileges(self):
        """Print the list of privileges."""
        print(f"Administrator Privileges: {', '.join(self.privileges)}")

class Admin(User):
    """Represent aspects of a user specific to an administrator."""
    
    def __init__(self, first_name, last_name):
        """Initialize attributes of the parent class and admin."""
        super().__init__(first_name, last_name)
        self.privileges = Privileges()  # Create an instance of Privileges
        
# Create an instance of Admin
admin_user = Admin("Bob", "Johnson")
admin_user.describe_user()
admin_user.privileges.show_privileges()  # Call the method from the Privileges instance
