import random

# Create a list of 10 numbers and 5 letters
lottery_pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']

# Randomly select four numbers or letters from the list
winning_numbers = random.sample(lottery_pool, 4)

print("Winning numbers or letters:", winning_numbers)
print("Any ticket matching these four numbers or letters wins a prize!")
