filename = './Chapter10/10_1_LearningPython/learning_python.txt'

with open(filename) as file:
    lines = file.readlines()

print("\nReplacing 'Python' with 'C':\n")
for line in lines:
    modified_line = line.replace('Python', 'C')
    print(modified_line.strip())
