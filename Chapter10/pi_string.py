# Working with a File's Contents
print("\nWorking with a File's Contents")

filename = "./Chapter10/pi_digits.txt"

with open(filename) as file_object:
    lines = file_object.readlines()
    
pi_string = ''
for line in lines:
    pi_string += line.strip()
    
print(pi_string)
print(len(pi_string))

# Large Files: One Million Digits
print("\nLarge Files: One Million Digits")

filename = "./Chapter10/pi_million_digits.txt"

with open(filename) as file_object:
    lines = file_object.readlines()
    
pi_string = ''
for line in lines:
    pi_string += line.strip()
    
print(f"{pi_string[:52]}...")
print(len(pi_string))

# Is Your Birthday Contained in Pi?
print("\nIs Your Birthday Contained in Pi?")

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")