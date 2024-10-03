# Importing functions from printing_functions.py
import printing_models2 as pf

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Calling the functions from the imported module
pf.print_models(unprinted_designs, completed_models)
pf.show_completed_models(completed_models)
