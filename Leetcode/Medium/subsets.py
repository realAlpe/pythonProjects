class Solution:
    """https://leetcode.com/problems/subsets/"""

    def subsets(self, nums: list[int]) -> list[list[int]]:
        if len(nums) == 0:
            return [[]]

        # recurse through the smaller number set
        num = nums.pop()
        prev = self.subsets(nums)
        # construct the missing lists off of the previous result
        # where we add to a list in the previous result, if the number is not in it yet
        missing = [lst + [num] for lst in prev if num not in lst]

        return prev + missing
