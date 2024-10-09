class Employee:
    def __init__(self, first_name, last_name, annual_salary):
        """Initialize the employee's attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, amount=5000):
        """Add the specified amount to the annual salary."""
        self.annual_salary += amount