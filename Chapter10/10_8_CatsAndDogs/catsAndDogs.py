def read_file(filename):
    try:
        with open("./Chapter10/10_8_CatsAndDogs/" + filename) as file:
            contents = file.read()
            print(f"\nContents of {filename}:\n{contents}")
    except FileNotFoundError:
        print(f"Sorry, the file {filename} was not found.")

# Reading the files
read_file('cats.txt')
read_file('dogs.txt')
