#!/usr/bin/env python3
# Fizz Buzz en Python

# Iteramos desde 1 hasta 100
for num in range(1, 101):
    # Comprobamos si el número es divisible por 3 y 5
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    # Comprobamos si el número es divisible por 3
    elif num % 3 == 0:
        print("Fizz")
    # Comprobamos si el número es divisible por 5
    elif num % 5 == 0:
        print("Buzz")
    # Si no es divisible ni por 3 ni por 5, imprimimos el número
    else:
        print(num)
