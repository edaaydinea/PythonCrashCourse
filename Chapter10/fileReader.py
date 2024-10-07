# Reading an entire file
print("Reading an entire file")

with open('./Chapter10/pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())
    
# Reading line by line
print("\nReading line by line")

filename = "./Chapter10/pi_digits.txt"

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())
        
        
# Making a list of lines from a file
print("\nMaking a list of lines from a file")

filename = "./Chapter10/pi_digits.txt"

with open(filename) as file_object:
    lines = file_object.readlines()
    
for line in lines:
    print(line.rstrip())
    