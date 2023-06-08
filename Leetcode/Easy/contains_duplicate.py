class Solution:
    """https://leetcode.com/problems/contains-duplicate/"""

    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(nums) != len(set(nums))
