current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

print("-------------------")

x = 1
while x <= 5:
    print(x)
    x += 1

# This loop will run forever!
# x = 1
# while x <= 5:
#     print(x)
