class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        length = len(nums)
        result = [1] * length
        prefix_product = 1
        postfix_product = 1
        for i in range(length):
            # Calculation for prefix
            result[i] *= prefix_product
            prefix_product = prefix_product * nums[i]

            # Calculation for postfix
            result[length - 1 - i] *= postfix_product
            postfix_product = postfix_product * nums[length - 1 - i]
        return result
