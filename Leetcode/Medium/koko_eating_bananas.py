class Solution:
    """https://leetcode.com/problems/koko-eating-bananas/"""

    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        def get_hours(k: int) -> int:
            return sum(1 + (pile - 1) // k for pile in piles)

        def binary_search(left: int, right: int) -> int:
            if left > right:
                return left
            m = (left + right) // 2
            if m == 0:  # (l, r)=(0, 0) OR (l, r)=(0, 1)
                return 1 if get_hours(1) <= h else 2
            if get_hours(m) <= h:
                return binary_search(left, m - 1)
            else:
                return binary_search(m + 1, right)

        return binary_search(0, max(piles) + 1)
