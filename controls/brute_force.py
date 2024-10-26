import copy
from time import sleep

from controls.movement import go_forward, go_backward
from model.board import Board
from model.cell import Cell
from view.show_board import show_board


def brute_force(board: Board):
    copied_board = copy.deepcopy(board)
    show_board(copied_board, loop_counter=0)
    copied_board.clean_values()
    sleep(5)
    row_index = 0
    col_index = 0
    direction = "forward"
    loop_counter = 0
    while True:
        loop_counter += 1
        show_board(copied_board, row_index, col_index, loop_counter=loop_counter)
        sleep(0.09)

        cell: Cell = copied_board.cells[row_index][col_index]
        if cell.is_pre_filled:
            if direction == "forward":
                try:
                    row_index, col_index = go_forward(row_index, col_index)
                except:
                    show_board(copied_board, loop_counter=loop_counter)
                    return copied_board
            else:
                try:
                    row_index, col_index = go_backward(row_index, col_index)
                except:
                    direction = "forward"

        else:
            try:
                cell.set_next_value()

                if copied_board.is_value_possible(cell):
                    direction = "forward"
                    try:
                        row_index, col_index = go_forward(row_index, col_index)
                    except:
                        show_board(copied_board, loop_counter=loop_counter)
                        return copied_board
            except:
                direction = "backward"
                row_index, col_index = go_backward(row_index, col_index)
