class User:
    def __init__(self, first_name, last_name, age, location):
        """Initialize user attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
    
    def describe_user(self):
        """Print a summary of the user's information."""
        print(f"User Information:\nName: {self.first_name} {self.last_name}\nAge: {self.age}\nLocation: {self.location}")
    
    def greet_user(self):
        """Print a personalized greeting to the user."""
        print(f"Hello, {self.first_name} {self.last_name}! Welcome back!")

# Creating instances of the User class
user_1 = User('John', 'Doe', 28, 'New York')
user_2 = User('Alice', 'Smith', 34, 'London')
user_3 = User('Maya', 'Jones', 22, 'Sydney')

# Call methods for each user
user_1.describe_user()
user_1.greet_user()

user_2.describe_user()
user_2.greet_user()

user_3.describe_user()
user_3.greet_user()
