#!/usr/bin/env python3
import sys

while True:
    argumentos = sys.argv
    print("¡Bienvenido a la calculadora básica! Por favor, ingrese la operación que desea realizar o 'salir' para salir.")

    operacion = input("Operación (por ejemplo, '2 + 2'): ")

    if operacion.lower() == 'salir':
        print("¡Hasta luego!")
        break

    try:
        resultado = eval(operacion)  # Utilizamos eval para evaluar la expresión ingresada
        print("Resultado:", resultado)
    except Exception as e:
        print("Error:", e)
