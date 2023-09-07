#!/usr/bin/env python3
"""
Exercise to practice List comprehension.

This script defines a function, dict_create, which takes two lists of cities and temperatures
and creates a dictionary that maps each city to its corresponding temperature.
"""

# List of cities
cities = ["cali", "medellin", "bogota"]

# List of temperatures
temperatures = ["24°", "18°", "10°"]

def dict_create(cities, temperatures) -> dict:
    """
    Create a dictionary mapping cities to temperatures.

    Args:
        cities (list): A list of city names.
        temperatures (list): A list of temperature values.

    Returns:
        dict: A dictionary where city names are keys and temperature values are values.
    """
    # Use a dictionary comprehension to create the mapping
    return {city: temp for city, temp in zip(cities, temperatures)}

# Call the function and store the result in a dictionary named "new_dict"
new_dict = dict_create(cities, temperatures)

# Print the resulting dictionary
print(new_dict)
