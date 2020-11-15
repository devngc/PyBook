"""This script demonstrates how to work with system path variables
through Python"""

import os
import sys
import functions

# Print all the environmental variables
variables = os.getenv("PATH").split(";")
print(variables)

# Appending the file path to the function to the evironmental variables
sys.path.append("G:\Dropbox\Github\PyBook\\functions.py")
functions.main()
