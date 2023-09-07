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
    # Create a dictionary using a dictionary comprehension
    # The keys are the numbers from list_random_nums
    # The values are "even" (even) or "odd" (odd) based on a conditional expression
    print({num: "even" if num % 2 == 0 else "odd" for num in [random.randint(0, 100) for _ in range(10)]})

# Call the dict_create function with the list of random numbers as an argument
dict_create()
