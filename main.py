import datetime

from controls.brute_force import brute_force
from model.board import Board
from sudoku_input_file import get_sudoku

if __name__ == '__main__':
    start_time = datetime.datetime.now()

    board = Board(get_sudoku())
    brute_force(board)

    total_time = datetime.datetime.now() - start_time

    print(f"Took {total_time.seconds} seconds to solve")
