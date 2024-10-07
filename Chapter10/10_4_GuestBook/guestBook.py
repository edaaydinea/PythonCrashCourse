filename = './Chapter10/10_4_GuestBook/guest_book.txt'

while True:
    name = input("Please enter your name (or type 'quit' to exit): ")
    
    if name.lower() == 'quit':
        break
    
    print(f"Hello, {name}! Welcome!")
    
    with open(filename, 'a') as file:
        file.write(f"{name}\n")
    
    print(f"Your visit has been recorded in {filename}.\n")
