# Saving each exercise as a separate file

# Exercise 2-3: Personal Message
personal_message = """
# Exercise 2-3: Personal Message
name = "Eric"
print(f"Hello {name}, would you like to learn some Python today?")
"""
with open("personal_message.py", "w") as f:
    f.write(personal_message)

# Exercise 2-4: Name Cases
name_cases = """
# Exercise 2-4: Name Cases
name = "Eric"
print(name.lower())
print(name.upper())
print(name.title())
"""
with open("name_cases.py", "w") as f:
    f.write(name_cases)

# Exercise 2-5: Famous Quote
famous_quote = """
# Exercise 2-5: Famous Quote
print('Albert Einstein once said, "A person who never made a mistake never tried anything new."')
"""
with open("famous_quote.py", "w") as f:
    f.write(famous_quote)

# Exercise 2-6: Famous Quote 2
famous_quote_2 = """
# Exercise 2-6: Famous Quote 2
famous_person = "Albert Einstein"
message = f'{famous_person} once said, "A person who never made a mistake never tried anything new."'
print(message)
"""
with open("famous_quote_2.py", "w") as f:
    f.write(famous_quote_2)

# Exercise 2-7: Stripping Names
stripping_names = """
# Exercise 2-7: Stripping Names
name = "\\t\\nEric\\t\\n"
print(f"Original name with whitespace: {repr(name)}")
print(f"Using lstrip(): {repr(name.lstrip())}")
print(f"Using rstrip(): {repr(name.rstrip())}")
print(f"Using strip(): {repr(name.strip())}")
"""
with open("stripping_names.py", "w") as f:
    f.write(stripping_names)

"/Chapter2 files have been successfully created!"
