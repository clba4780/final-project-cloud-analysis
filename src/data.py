from core import list_variables

""" Goal: Load data from the data_access submodule
Variables to access: 
a) 
b) 
.
.
.
"""

"""
Part 1:Accessing
- Access data from data_access
"""

"""
Part 2: cleaning
- handle missing values
- handle conversion (if necessary)
- select time and spatial region
"""

# list of all atmospheric variables
print(list_variables("atm", "historical", "cmip6"))