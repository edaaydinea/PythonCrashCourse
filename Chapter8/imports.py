# 1. Import the entire module
import greet_functions
greet_functions.greet_user('Jane')

# 2. Import a specific function from the module
from greet_functions import greet_user
greet_user('Sam')

# 3. Import the function with an alias
from greet_functions import greet_user as gu
gu('Lauren')

# 4. Import the module with an alias
import greet_functions as gf
gf.greet_user('Sophia')

# 5. Import all functions from the module
from greet_functions import *
greet_user('Ella')
