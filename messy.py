import os
import sys  # Ruff will hate that these are on separate lines or unused


def MyFunction(name):
    # Ruff will flag the CamelCase name and the extra spaces
    if name == None:
        return "No name"
    else:
        return "Hello " + name
