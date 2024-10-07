filename = "./Chapter10/10_1_LearningPython/learning_python.txt"

# Reading the entire file and printing its contents
with open(filename) as file:
    contents = file.read()
    print("Reading an entire file:\n")
    print(contents)
    
# Looping over the file object to print each line
print("\nReading line be line with a loop:\n")
with open(filename) as file:
    for line in file:
        print(line.strip())
        
# Storing the lines in a list and printing them outside the with block
print("|nReading and storing lines in a list:\n")
with open(filename) as file:
    lines = file.readlines()
    
for line in lines:
    print(line.strip())