#!/usr/bin/env python3
"""
Exercise to practice List comprehension.

This script defines a function, dict_create, which takes a list of words and creates a dictionary that maps each word to its corresponding length.

¬ - - - - - - - - - - - - - - - - - - - - - - - - - - -  ¬
| This is the code we saved ourselves:                   |
|                                                        |
|  dict_length = {}                                      |
|    for word in list:                                   |
|        dict_length[word] = len(word)                   |
|    return dict_length                                  |
|                                                        |
|  result = dict_create(list)                            |
|  print(result)                                         |
¬ - - - - - - - - - - - - - - - - - - - - - - - - - - -  ¬
"""

# Create a list of words
list = ["software", "code", "linux"]

# Define a function called dict_create that takes a list as an argument
def dict_create(list) -> dict:
    # Use a dictionary comprehension to create a dictionary
    # The key is each word in the list, and the value is the length of the word
    return print({word: len(word) for word in list})

# Call the dict_create function with the provided list
dict_create(list)
