from model.cell import Cell


class Board:
    def __init__(self, values):
        self.cells = []
        if type(values) is str:
            values = self.convert_to_list(values)

        for row, line in enumerate(values):
            self.cells.append([])
            for col, cell in enumerate(line):
                self.cells[row].append(Cell(row, col, cell))

    @staticmethod
    def convert_to_list(values) -> list:
        temp_values = []

        for i in range(len(values)):
            if i % 9 == 0:
                new_line = []

            new_line.append(int(values[i]))

            if i % 9 == 8:
                temp_values.append(new_line)
        return temp_values

    def get_row(self, index: int) -> list:
        return self.cells[index].copy()

    def get_col(self, index):
        return [line[index] for line in self.cells]

    @staticmethod
    def get_square_index(row, col):
        return (row // 3) * 3 + (col // 3)

    def get_square(self, index):
        row_start = (index // 3) * 3
        col_start = (index % 3) * 3
        square = []
        for i in range(3):
            for j in range(3):
                square.append(self.cells[row_start + i][col_start + j])

        return square

    @staticmethod
    def has_repeated_element(lst):
        seen = set()
        for item in lst:
            if item in seen:
                return True
            if item != 0:
                seen.add(item)
        return False

    def is_value_possible(self, cell: Cell):
        if cell.value == 0:
            raise ValueError("Cell value cannot be 0")

        row_index = cell.position_horizontal
        col_index = cell.position_vertical
        square_index = self.get_square_index(row_index, col_index)

        if self.has_repeated_element([i.value for i in self.get_row(row_index)]):
            return False

        if self.has_repeated_element([i.value for i in self.get_col(col_index)]):
            return False

        if self.has_repeated_element([i.value for i in self.get_square(square_index)]):
            return False

        return True

    def clean_values(self):
        removed_numbers = 0
        for line in self.cells:
            for cell in line:
                if not cell.is_pre_filled:
                    temp_possible_values = cell.possible_values.copy()
                    for value in temp_possible_values:
                        cell.value = value
                        if not self.is_value_possible(cell):
                            cell.remove_possible_value(value)
                            removed_numbers += 1
                        cell.value = 0
        print("Removed " + str(removed_numbers) + " numbers")
