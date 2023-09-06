from enum import Enum

# Definimos una enumeración para los movimientos posibles
class Movement(Enum):
    DOWN = 1
    RIGHT = 2
    LEFT = 3
    ROTATE = 4 

# Definimos la pantalla del juego Tetris
def tetris():
    # Creamos una pantalla de 10x10 representada como una lista de listas
    screen = [
        ["🔳", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"],
        ["🔳", "🔳", "🔳", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"],
        ["🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"],
        ["🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"],
        ["🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"],
        ["🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"],
        ["🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"],
        ["🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"],
        ["🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"],
        ["🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"]
    ]

    print_screen(screen)

    # Mueve la pieza completa hacia abajo tres veces
    for _ in range(3):
        screen = move_piece(screen, Movement.DOWN)

# Función para imprimir la pantalla del juego
def print_screen(screen: list):
    print("\nPantalla Tetris:\n")
    for row in screen:
        print(" ".join(map(str, row)))

# Función para mover la pieza en la pantalla
def move_piece(screen: list, movement: Movement):
    new_screen = [["🔲"] * 10 for _ in range(10)]

    for row_index, row in enumerate(screen):
        for column_index, item in enumerate(row):
            if item == "🔳":
                if movement == Movement.DOWN:
                    new_row_index = row_index + 1
                    new_column_index = column_index
                elif movement == Movement.RIGHT:
                    new_row_index = row_index
                    new_column_index = column_index + 1
                elif movement == Movement.LEFT:
                    new_row_index = row_index
                    new_column_index = column_index - 1
                elif movement == Movement.ROTATE:
                    # Agregar rotación de pieza
                    pass
                    
                if 0 <= new_row_index < 10 and 0 <= new_column_index < 10:
                    new_screen[new_row_index][new_column_index] = "🔳"

    print_screen(new_screen)
    return new_screen

tetris()
