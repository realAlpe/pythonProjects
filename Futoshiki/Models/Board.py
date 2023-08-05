from Futoshiki.Models.EdgeType import EdgeType
from Futoshiki.Models.TypeSynonyms import Position, Edge


class Board:
    def __init__(self, size: int):
        self.size = size
        self._b: dict[Position, int] = {(i, j): 0 for i in range(self.size) for j in range(self.size)}
        self._e: set[Edge] = set()

    def _position_in_bounds(self, position: Position) -> bool:
        r, c = position
        return 0 <= r < self.size and 0 <= c < self.size

    def _value_in_bounds(self, value: int) -> bool:
        return 0 < value <= self.size

    def _are_adjacent(self, position1: Position, position2: Position) -> bool:
        r1, c1 = position1
        r2, c2 = position2
        return (self._position_in_bounds(position1)
                and self._position_in_bounds(position2)
                and abs(r1 - r2) + abs(c1 - c2) <= 1)

    def set_value(self, position: Position, value: int) -> bool:
        if not self._position_in_bounds(position) or not self._value_in_bounds(value):
            return False

        self._b[position] = value
        return True

    def set_edge(self, position1: Position, edge_type: EdgeType, position2: Position) -> bool:
        if not self._are_adjacent(position1, position2):
            return False

        self._e.add((position1, edge_type, position2))
        self._e.add((position2, edge_type.swap(), position1))
        return True

    def get_edge_type_or_none(self, position1: Position, position2: Position) -> EdgeType | None:
        if (position1, EdgeType.GT, position2) in self._e:
            return EdgeType.GT
        if (position1, EdgeType.LT, position2) in self._e:
            return EdgeType.LT
        return None

    def _row_to_string(self, row: int) -> str:
        s = "| "
        for col in range(self.size):
            # display value
            pos = (row, col)
            value = self._b[pos]
            s += f"{value} "

            # display edge
            edge_type = self.get_edge_type_or_none(pos, (row, col + 1))
            if edge_type:
                s += f"{edge_type.to_unicode()} "
            else:
                s += "  "

        return s[:-2] + "|\n"

    def _between_rows_to_string(self, row: int) -> str:
        s = "| "
        for col in range(self.size):
            pos1 = (row, col)
            pos2 = (row + 1, col)

            edge_type = self.get_edge_type_or_none(pos1, pos2)
            if edge_type:
                s += f"{edge_type.to_unicode(True)}   "
            else:
                s += "    "
        return s[:-2] + "|\n"

    def is_valid_board(self) -> bool:
        # check rows and columns
        for k in range(self.size):
            row = [self._b[(k, j)] for j in range(self.size) if self._b[(k, j)] != 0]
            if len(row) != len(set(row)):
                return False

            col = [self._b[(i, k)] for i in range(self.size) if self._b[(i, k)] != 0]
            if len(col) != len(set(col)):
                return False

        # check edge conditions
        for edge in self._e:
            (p1, edge_type, p2) = edge
            v1 = self._b[p1]
            v2 = self._b[p2]
            if v1 == 0 or v2 == 0:
                continue

            if edge_type == EdgeType.LT and (v1 == self.size + 1 or not v1 < v2):
                return False
            if edge_type == EdgeType.GT and (v2 == self.size + 1 or not v1 > v2):
                return False

        return True

    def get_empty_position(self) -> Position | None:
        for i in range(self.size):
            for j in range(self.size):
                if self._b[i, j] == 0:
                    return i, j
        return None

    def solve(self) -> bool:
        pos = self.get_empty_position()
        if pos is None:
            return True

        for v in range(0, self.size):
            self._b[pos] = v + 1

            if self.is_valid_board() and self.solve():
                return True

            self._b[pos] = 0

        return False

    def __str__(self):
        bar = "- " * (2 * self.size + 1)
        res = f"{bar}\n"
        for i in range(self.size - 1):
            res += self._row_to_string(i)
            res += self._between_rows_to_string(i)
        res += self._row_to_string(self.size - 1)
        res += bar
        return res
