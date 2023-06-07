from dataclasses import dataclass
from pprint import pprint


@dataclass
class Cell:
    group_id: int
    value: int = 0
    max_size: int = 0


@dataclass
class Board:
    cells: list[list[Cell]]

    def __post_init__(self):
        self.width = len(self.cells)
        self.height = len(self.cells[0])

    @classmethod
    def parse_board(cls, input_board: str):
        cells = [
            [Cell(int(group_id_str)) for group_id_str in row.split()]
            for row in (input_board.strip().split("\n"))
        ]

        group_id_to_max_size = dict()
        for cell_row in cells:
            for cell in cell_row:
                if cell.group_id in group_id_to_max_size:
                    group_id_to_max_size[cell.group_id] += 1
                else:
                    group_id_to_max_size[cell.group_id] = 1

        for cell_row in cells:
            for cell in cell_row:
                cell.max_size = group_id_to_max_size[cell.group_id]

        return cls(cells)

    def get_adjacent_cell_values(self, row: int, col: int) -> set[int]:
        return {
            self.cells[i][j].value
            for i in range(row - 1, row + 2)
            for j in range(col - 1, col + 2)
            if 0 <= i < self.width and 0 <= j < self.height and (i != row or j != col)
        }

    def solve_board(self) -> bool:
        pos = self.get_next_empty()
        if pos is None:
            return True
        row, col = pos
        cell = self.cells[row][col]
        for v in range(1, cell.max_size + 1):
            if self.valid_placement(pos, v):
                cell.value = v
                pprint(self)

                if self.solve_board():
                    return True

                cell.value = 0

        return False

    def valid_placement(self, pos: tuple[int, int], new_value: int) -> bool:
        row, col = pos
        cell = self.cells[row][col]
        if not (1 <= new_value <= cell.max_size) \
                or new_value in self.get_values_of_group(cell.group_id) \
                or new_value in self.get_adjacent_cell_values(row, col):
            return False
        return True

    def get_values_of_group(self, group_id: int) -> set[int]:
        return {
            cell.value
            for cell_row in self.cells
            for cell in cell_row
            if cell.group_id == group_id
        }

    def get_next_empty(self) -> tuple[int, int] | None:
        for i, cell_row in enumerate(self.cells):
            for j, cell in enumerate(cell_row):
                if cell.value == 0:
                    return i, j
        return None


def value_in_size(cell: Cell, max_size: int) -> bool:
    return 1 <= cell.value <= max_size


def unique_value_in_list(cell: Cell, lst: list[Cell]) -> bool:
    return cell.value not in {cell.value for cell in lst}


def main():
    input_board = '''
    2 3 3 1 1 1
    2 4 4 4 1 1
    5 5 4 4 4 1
    5 2 6 6 6 1
    5 7 7 6 1 8
    7 7 7 7 8 8
    '''
    b = Board.parse_board(input_board)
    pprint(b)
    b.solve_board()
    pprint(b)


if __name__ == '__main__':
    main()
