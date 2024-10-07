def read_file(filename):
    try:
        with open("./Chapter10/10_8_CatsAndDogs/" +filename) as file:
            contents = file.read()
            print(f"\nContents of {filename}:\n{contents}")
    except FileNotFoundError:
        pass  # Silently fails if the file is missing

# Reading the files
read_file('cats.txt')
read_file('dogs.txt')
