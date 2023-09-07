#!/usr/bin/env python3
"""
Exercise to practice List comprehension.

This script defines a function, dict_create, which takes a list of numbers and creates a dictionary that maps each number to its parity (even or odd).

¬ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -¬
| This is the code we saved ourselves:                                   |
|                                                                        |
|  result_dict = {}                                                      |
|                                                                        |
|    # Iterate through the list of random numbers                        |
|    for num in list_random_nums:                                        |
|        # Determine if the number is even or odd                        |
|        if num % 2 == 0:                                                |
|            result_dict[num] = "even"  # If even, add to the dictionary |
|            with "par" as the value                                     |
|        else:                                                           |
|            result_dict[num] = "odd"  # If odd, add to the dictionary   |
|            with "impar" as the value                                   |
|                                                                        |
|    # Return the resulting dictionary                                   |
|    return result_dict                                                  |
¬ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -¬
"""
# Import the random module to generate random numbers
import random

# Set the length of the list
list_length = 10

# Define the minimum and maximum values for random number generation
min_value = 0
max_value = 100

# Generate a list of random numbers using a list comprehension
list_random_nums = [random.randint(min_value, max_value) for _ in range(list_length)]

# Define a function called dict_create that takes a list of numbers as input
def dict_create(list_random_nums) -> dict:
    # Create a dictionary using a dictionary comprehension
    # The keys are the numbers from list_random_nums
    # The values are "even" (even) or "odd" (odd) based on a conditional expression
    return print({num: "even" if num % 2 == 0 else "odd" for num in list_random_nums})

# Call the dict_create function with the list of random numbers as an argument
dict_create(list_random_nums)
