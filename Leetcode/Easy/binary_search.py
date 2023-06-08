class Solution:
    """https://leetcode.com/problems/binary-search/"""

    def search(self, nums: list[int], target: int) -> int:
        def binary_search(left: int, right: int) -> int:
            if left > right:
                return -1
            mid = (right + left) // 2
            value = nums[mid]
            if value > target:
                return binary_search(left, mid - 1)
            if value < target:
                return binary_search(mid + 1, right)
            return mid

        return binary_search(0, len(nums) - 1)
