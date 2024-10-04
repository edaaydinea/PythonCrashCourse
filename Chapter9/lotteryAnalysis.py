import random

# Create a list of 10 numbers and 5 letters for the lottery
lottery_pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'B', 'C', 'D', 'E']
my_ticket = [1, 'A', 5, 'C']  # Example ticket

# Loop until my_ticket matches the winning numbers
attempts = 0
while True:
    winning_numbers = random.sample(lottery_pool, 4)
    attempts += 1
    if set(my_ticket) == set(winning_numbers):
        break

print(f"It took {attempts} attempts to win with ticket {my_ticket}!")
