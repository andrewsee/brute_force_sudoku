import os

# ANSI color codes
RED = "\033[91m"
LIME_GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RESET = "\033[0m"


def show_board(board, current_row=None, current_col=None, loop_counter=0):
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console
    print(f"Loop counter: {loop_counter}")

    # Print the top border
    print("╔═══╤═══╤═══╦═══╤═══╤═══╦═══╤═══╤═══╗")

    for i, row in enumerate(board.cells):
        row_str = "║"
        for j, cell in enumerate(row):
            if cell.is_pre_filled:
                color = BLUE
            elif i == current_row and j == current_col:
                color = RED
            elif cell.value != 0:
                color = LIME_GREEN
            else:
                color = YELLOW

            row_str += f" {color}{cell.value if cell.value != 0 else ' '}{RESET} "

            if j % 3 == 2 and j < 8:
                row_str += "║"
            elif j < 8:
                row_str += "│"

        row_str += "║"
        print(row_str)

        if i == 2 or i == 5:
            print("╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣")
        elif i < 8:
            print("╟───┼───┼───╫───┼───┼───╫───┼───┼───╢")

    # Print the bottom border
    print("╚═══╧═══╧═══╩═══╧═══╧═══╩═══╧═══╧═══╝")
