def count_word_occurrences(filename, word):
    try:
        with open("./Chapter10/10_10_CommonWords/" +filename, encoding='utf-8') as file:
            contents = file.read().lower()
            word_count = contents.count(word)
            return word_count
    except FileNotFoundError:
        print(f"Sorry, the file {filename} was not found.")
        return 0

filename = 'pg74539.txt'
word = 'the '

# Count occurrences of 'the ' (with space to avoid counting 'then', 'there', etc.)
word_count = count_word_occurrences(filename, word)
print(f"The word '{word.strip()}' appears {word_count} times in {filename}.")
