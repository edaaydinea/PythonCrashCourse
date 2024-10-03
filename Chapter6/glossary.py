# A python dictionary can be used to model an actual dictionary.
# However, to avoid confusion, let's call it a glossary.
# Think of five programming words you've learned about in the previous chapters.
# Use these words as the keys in your glossary, and store their meanings as values.
# Print each word and its meaning as neatly formatted output.
# You can use the newline character (\n) to insert a blank line between each word-meaning pair.

glossary = {
    'list': 'A collection of items in a particular order.',
    'tuple': 'An immutable list.',
    'dictionary': 'A collection of key-value pairs.',
    'set': 'A collection of unique items.',
    'loop': 'A block of code that repeats a specific number of times.'
}

for word, meaning in glossary.items():
    print(f"{word.title()}: {meaning}\n")
    