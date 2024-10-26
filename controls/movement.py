def to_absolute_index(row: int, col: int) -> int:
    """
    Convert Sudoku row and column to an absolute index.

    Args:
    row (int): The row index (0-8)
    col (int): The column index (0-8)

    Returns:
    int: The absolute index (0-80)

    Raises:
    ValueError: If row or col is out of range
    """
    if not (0 <= row < 9 and 0 <= col < 9):
        raise ValueError("Row and column must be between 0 and 8")

    return row * 9 + col


def from_absolute_index(index: int) -> tuple[int, int]:
    """
    Convert an absolute index to Sudoku row and column.

    Args:
    index (int): The absolute index (0-80)

    Returns:
    tuple[int, int]: The (row, col) pair

    Raises:
    ValueError: If index is out of range
    """
    if not 0 <= index < 81:
        raise ValueError("Index must be between 0 and 80")

    row = index // 9
    col = index % 9
    return row, col


def go_forward(row_index: int, col_index: int) -> tuple[int, int]:
    index = to_absolute_index(row_index, col_index)
    index += 1
    return from_absolute_index(index)


def go_backward(row_index: int, col_index: int) -> tuple[int, int]:
    index = to_absolute_index(row_index, col_index)
    index -= 1
    return from_absolute_index(index)
