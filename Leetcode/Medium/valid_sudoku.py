from typing import Iterable


class Solution:
    """https://leetcode.com/problems/valid-sudoku/"""

    def isValidSudoku(self, board: list[list[str]]) -> bool:
        for row_idx in range(9):
            if not unique_elements(board[row_idx]):
                return False

        for col_idx in range(9):
            if not unique_elements(board[row_idx][col_idx] for row_idx in range(9)):
                return False

        for box_nr in range(9):
            d, r = divmod(box_nr, 3)
            if not unique_elements(board[row_idx][col_idx]
                                   for row_idx in range(3 * d, 3 * d + 3)
                                   for col_idx in range(3 * r, 3 * r + 3)
                                   ):
                return False
        return True


def unique_elements(iterable: Iterable[str]) -> bool:
    unique = set()
    for value in iterable:
        if value == ".":
            continue
        if value in unique:
            return False
        unique.add(value)
    return True
