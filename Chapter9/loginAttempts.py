class User:
    def __init__(self, first_name, last_name, age, location):
        """Initialize user attributes, including login attempts."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.login_attempts = 0  # Default value of 0
    
    def describe_user(self):
        """Print a summary of the user's information."""
        print(f"User Information:\nName: {self.first_name} {self.last_name}\nAge: {self.age}\nLocation: {self.location}")
    
    def greet_user(self):
        """Print a personalized greeting to the user."""
        print(f"Hello, {self.first_name} {self.last_name}! Welcome back!")
    
    def increment_login_attempts(self):
        """Increment the number of login attempts by 1."""
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        """Reset the number of login attempts to 0."""
        self.login_attempts = 0

# Create an instance of User
user = User('John', 'Doe', 28, 'New York')

# Increment login attempts several times
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()

# Print the number of login attempts
print(f"Login attempts: {user.login_attempts}")

# Reset login attempts and print the value again
user.reset_login_attempts()
print(f"Login attempts after reset: {user.login_attempts}")
