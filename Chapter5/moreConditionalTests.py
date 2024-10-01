"""

5-2. More Conditional Tests: You don’t have to limit the number of tests you
create to ten. If you want to try more comparisons, write more tests and add
them to conditional_tests.py. Have at least one True and one False result for
each of the following:
• Tests for equality and inequality with strings
• Tests using the lower() method
• Numerical tests involving equality and inequality, greater than and
less than, greater than or equal to, and less than or equal to
• Tests using the and keyword and the or keyword
• Test whether an item is in a list
• Test whether an item is not in a list
"""

# Tests for equality and inequality with strings
print("Equality and inequality with strings")
print("Test 1: 'hello' == 'hello' is True")
print('hello' == 'hello')
print("Test 2: 'hello' == 'Hello' is False")
print('hello' == 'Hello')

# Tests using the lower() method
print("\nTests using the lower() method")
print("Test 3: 'Hello'.lower() == 'hello' is True")
print('Hello'.lower() == 'hello')
print("Test 4: 'Hello'.lower() == 'Hello' is False")
print('Hello'.lower() == 'Hello')

# Numerical tests involving equality and inequality, greater than and less than,
# greater than or equal to, and less than or equal to
print("\nNumerical tests involving equality and inequality, greater than and less than,")
print("greater than or equal to, and less than or equal to")
print("Test 5: 5 == 5 is True")
print(5 == 5)
print("Test 6: 5 != 6 is True")
print(5 != 6)
print("Test 7: 5 > 4 is True")
print(5 > 4)
print("Test 8: 5 < 4 is False")
print(5 < 4)
print("Test 9: 5 >= 5 is True")
print(5 >= 5)
print("Test 10: 5 <= 4 is False")
print(5 <= 4)

# Tests using the and keyword and the or keyword
print("\nTests using the and keyword and the or keyword")
print("Test 11: 5 == 5 and 5 > 4 is True")
print(5 == 5 and 5 > 4)
print("Test 12: 5 == 5 and 5 < 4 is False")
print(5 == 5 and 5 < 4)
print("Test 13: 5 == 5 or 5 < 4 is True")
print(5 == 5 or 5 < 4)
print("Test 14: 5 != 5 or 5 < 4 is False")
print(5 != 5 or 5 < 4)

# Test whether an item is in a list
print("\nTest whether an item is in a list")
print("Test 15: 'hello' in ['hello', 'world'] is True")
print('hello' in ['hello', 'world'])
print("Test 16: 'hello' in ['Hello', 'world'] is False")
print('hello' in ['Hello', 'world'])

# Test whether an item is not in a list
print("\nTest whether an item is not in a list")
print("Test 17: 'hello' not in ['Hello', 'world'] is True")
print('hello' not in ['Hello', 'world'])
print("Test 18: 'hello' not in ['hello', 'world'] is False")
print('hello' not in ['hello', 'world'])


