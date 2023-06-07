from dataclasses import dataclass
from pprint import pprint


@dataclass
class Cell:
    group_id: int
    row: int
    col: int
    value: int = 0


@dataclass
class Group:
    members: list[Cell]

    def __len__(self):
        return len(self.members)


@dataclass
class Board:
    cells: list[list[Cell]]
    groups: dict[int, Group] | None = None

    def __post_init__(self):
        self.width = len(self.cells)
        self.height = len(self.cells[0])

    @classmethod
    def parse_board(cls, input_board: str):
        groups: dict[int, Group] = {}
        cells: list[list[Cell]] = []
        for row_index, row in enumerate(input_board.strip().split("\n")):
            cell_row: list[Cell] = []

            for col_index, group_id_str in enumerate(row.split()):
                group_id = int(group_id_str)
                cell = Cell(group_id=group_id, row=row_index, col=col_index)
                cell_row.append(cell)

                if group_id in groups:
                    groups[group_id].members.append(cell)
                else:
                    groups[group_id] = Group(members=[cell])

            cells.append(cell_row)

        return cls(cells=cells, groups=groups)

    def is_valid_board(self) -> bool:
        return all(
            value_in_size(cell, len(self.groups[cell.group_id]))  # valid size
            and unique_value_in_list(cell, self.groups[cell.group_id].members)  # unique in group
            and unique_value_in_list(cell, self.get_adjacent_cells(cell))  # unique in adjacent cells
            for cell_row in self.cells
            for cell in cell_row
        )

    def get_adjacent_cells(self, cell: Cell) -> list[Cell]:
        row = cell.row
        col = cell.col
        return [
            self.cells[i][j]
            for i in range(row - 1, row + 2)
            for j in range(col - 1, col + 2)
            if 0 <= i < self.width and 0 <= j < self.height and (i != row or j != col)
        ]

    def update_values(self, old_cell: Cell, new_cell: Cell):
        self.cells[new_cell.row][new_cell.col] = new_cell
        idx = self.groups[new_cell.group_id].members.index(old_cell)
        self.groups[new_cell.group_id].members[idx] = new_cell

    def solve_board(self) -> bool:
        cell = self.get_next_empty_cell()
        if cell is None:
            return True
        max_size = len(self.groups[cell.group_id])

        for v in range(1, max_size + 1):
            c = Cell(cell.group_id, cell.row, cell.col, v)
            if self.valid_placement(c):
                self.cells[cell.row][cell.col] = c

                if self.solve_board():
                    return True

                self.cells[cell.row][cell.col] = cell

        return False

    def valid_placement(self, cell: Cell) -> bool:
        group = self.groups[cell.group_id]
        max_size = len(group)
        if not (1 <= cell.value <= max_size) \
                or cell.value in {c.value for c in group.members} \
                or cell.value in {c.value for c in self.get_adjacent_cells(cell)}:
            return False
        return True

    def get_next_empty_cell(self) -> Cell | None:
        for cell_row in self.cells:
            for cell in cell_row:
                if cell.value == 0:
                    return cell
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
