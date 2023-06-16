class Solution:
    """https://leetcode.com/problems/product-of-array-except-self/"""

    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # kinda difficult to explain but O(1) space complexity but not O(n) time complexity
        fst = nums[0]
        nums[0], nums[1] = nums[1], nums[0]
        for i in range(2, len(nums)):
            last = fst * nums[0]
            for k in range(i):
                nums[k] *= nums[i]
            nums[i] = last
        return nums


""" 
# recursive approach, O(n) space complexity but not O(n) time complexity
def productExceptSelf(self, nums: list[int]) -> list[int]:
    if len(nums) == 2:
        return [nums[1], nums[0]]

    fst = nums[0]
    res = [nums[1], nums[0]]
    for i in range(2, len(nums)):
        num = nums[i]
        last = fst * res[0]
        res = [x * num for x in res]
        res.append(last)
    print(res)
"""
