#!/usr/bin/env python3
"""
Exercise to practice List comprehension.

This script defines a function, dict_create, which takes a list of numbers and creates a dictionary that maps each number to its cube.

¬ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -¬
| This is the code we saved ourselves:                                   |
|                                                                        |
|  def dict_create(nums) -> dict:                                        |
|     cubo = {}                                                          |
|     for num in nums:                                                   |
|        cubo[num] = num ** 3                                            |
|     return cubo                                                        |
¬ - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -¬
"""


def dict_create() -> dict:
    """
    Creates a dictionary that maps each number to its cube.

    Args:
    nums (list): A list of numbers.

    Returns:
    dict: A dictionary where keys are numbers and values are their cubes.
    """
    #Returning and printing the dict
    return print({num: num **3 for num in range(1, 11)})

dict_create()
