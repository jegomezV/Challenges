#!/usr/bin/env python3
"""
Exercise to practice List comprehension.

This script defines a function, print_str, which takes a list of countries and prints a formatted list of countries with indices and separators.

Functions:
    print_str(countries):
        Creates a formatted list of countries with indices and separators.

Args:
    countries (list): A list of country names to be formatted and printed.

Returns:
    None

Additional Details:
    This script demonstrates the use of list comprehension to format and display a list of countries with their respective indices. The formatted output consists of a separator line, each country's index, name, and a separator line at the end. The purpose is to showcase how to manipulate and present data in a readable format.

¬ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -¬
| This is the code we saved ourselves:                                                         |
|                                                                                              |
| print("\n")                                                                                  |
| print("-----------------------------------------------------------------------------\n")     |
| print("\n")                                                                                  |
| str = ""                                                                                     |
| for index, country in enumerate(countries):                                                  |
|     str += "{} - {}".format(index + 1, country)                                              |
|     if index < len(countries) - 1:                                                           |
|         str += "\n"                                                                          |
| print(str)                                                                                   |
| print("-----------------------------------------------------------------------------\n")     |                                                 |
¬ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -¬

"""
countries = ["Canada", "USA", "Mexico", "Australia"]

def print_str(countries):
    """
    Creates a formatted list of countries with indices and separators.

    Args:
        countries (list): A list of country names.

    Returns:
        None
    """
    print("{}\n{}\n\n{}".format("-" * 78, "\n".join(["{}({}) -> {}.".format(" " * 30, index + 1, country) for index, country in enumerate(countries)]), "-" * 78))

# Call the print_str function with the list of countries
print_str(countries)
