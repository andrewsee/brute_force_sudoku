class PrefilledCellException(Exception):
    pass


class NoRemainingSolutionException(Exception):
    pass


class Cell:
    def __init__(self, position_horizontal, position_vertical, value):
        self.position_horizontal: int = position_horizontal
        self.position_vertical: int = position_vertical
        self.value: int = value
        self.is_pre_filled: bool = value != 0
        self.possible_values: list = [value] if self.is_pre_filled else [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def set_next_value(self):
        if self.is_pre_filled:
            raise NoRemainingSolutionException("Tried to change pre set value")

        if self.value == 0:
            self.value = self.possible_values[0]
        else:
            next_index = self.possible_values.index(self.value) + 1
            if next_index >= len(self.possible_values):
                self.value = 0
                raise NoRemainingSolutionException()
            self.value = self.possible_values[next_index]

    def remove_possible_value(self, value):
        if self.is_pre_filled:
            raise PrefilledCellException()
        if value in self.possible_values and len(self.possible_values) == 1:
            raise NoRemainingSolutionException()
        self.possible_values.remove(value)
