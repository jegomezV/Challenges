#!/usr/bin/env python3
"""
Exercise to practice List comprehension.

This script defines a function, dict_create, which takes a list of numbers and creates a dictionary that maps each number to its parity (even or odd).

¬ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -¬
| This is the code we saved ourselves:                                   |
|                                                                        |
|  def dict_create():                                                    |
|    result_dict = {}                                                    |
|                                                                        |
|    random_nums = [random.randint(0, 100) for _ in range(10)]           |
|                                                                        |
|    for num in random_nums:                                             |
|        if num % 2 == 0:                                                |
|            result_dict[num] = "even"                                   |
|        else:                                                           |
|            result_dict[num] = "odd"                                    |
|                                                                        |
|    print(result_dict)                                                  |
|                                                                        |
|dict_create()                                                           |
¬ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -¬
"""
# Import the random module to generate random numbers
import random

# Define a function called dict_create that takes a list of numbers as input
def dict_create():
    # Create an empty dictionary
    result_dict = {}

    # Generate a list of 10 random numbers
    random_nums = [random.randint(0, 100) for _ in range(10)]

    # Loop through the random numbers
    for num in random_nums:
        # Check if the number is even or odd and add it to the dictionary
        if num % 2 == 0:
            result_dict[num] = "even"
        else:
            result_dict[num] = "odd"
    
    # Print the resulting dictionary
    print(result_dict)

# Call the dict_create function
dict_create()
