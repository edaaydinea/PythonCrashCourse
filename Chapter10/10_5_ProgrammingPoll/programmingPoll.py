filename = './Chapter10/10_5_ProgrammingPoll/programmingPoll.txt'

while True:
    reason = input("Why do you like programming? (or type 'quit' to exit): ")
    
    if reason.lower() == 'quit':
        break
    
    with open(filename, 'a') as file:
        file.write(f"{reason}\n")
    
    print("Thank you for your response!\n")


# Output:
# Why do you like programming? (or type 'quit' to exit): I love programming because it is fun.
# Thank you for your response!