
# Exercise 2-7: Stripping Names
name = "\t\nEric\t\n"
print(f"Original name with whitespace: {repr(name)}")
print(f"Using lstrip(): {repr(name.lstrip())}")
print(f"Using rstrip(): {repr(name.rstrip())}")
print(f"Using strip(): {repr(name.strip())}")
