class Solution:
    """https://leetcode.com/problems/search-a-2d-matrix/"""

    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        # find the row such that row[0] < target < row[-1]
        def binary_search_row(top: int, bottom: int) -> int:
            if top > bottom:
                return -1
            mid = (top + bottom) // 2
            lvalue = matrix[mid][0]
            rvalue = matrix[mid][-1]
            if target < lvalue:
                return binary_search_row(top, mid - 1)
            if target > rvalue:
                return binary_search_row(mid + 1, bottom)
            return mid
        
        # usual binary search for a given list (here matrix[row])
        def binary_search_col(left: int, right: int) -> bool:
            if left > right:
                return False
            mid = (right + left) // 2
            value = matrix[row][mid]
            if value > target:
                return binary_search_col(left, mid - 1)
            if value < target:
                return binary_search_col(mid + 1, right)
            return True

        row = binary_search_row(0, len(matrix) - 1)
        if row == -1:
            return False
        return binary_search_col(0, len(matrix[0]))
