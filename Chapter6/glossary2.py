# Step 1: Create the glossary
glossary = {
    'variable': 'A symbol that holds data or a reference to data.',
    'function': 'A block of reusable code that performs a specific task.',
    'list': 'A collection of items in a particular order, enclosed in square brackets.',
    'dictionary': 'A collection of key-value pairs, enclosed in curly braces.',
    'loop': 'A sequence of instructions that is continually repeated until a certain condition is met.'
}

# Step 3: Add five more terms to the glossary
glossary['tuple'] = 'An immutable list, enclosed in parentheses.'
glossary['set'] = 'A collection of unique items, without any order.'
glossary['class'] = 'A blueprint for creating objects (instances) that encapsulate both data and behaviors.'
glossary['module'] = 'A file containing Python code that can be imported into another Python program.'
glossary['list comprehension'] = 'A concise way to create lists based on existing lists using a single line of code.'

# Step 2: Loop through the dictionary and print terms with their meanings
for term, meaning in glossary.items():
    print(f"{term.title()}: {meaning}\n")
