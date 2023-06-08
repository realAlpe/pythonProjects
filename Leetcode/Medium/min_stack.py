import bisect


class MinStack:
    """https://leetcode.com/problems/min-stack/"""

    def __init__(self):
        self.stack = list()
        self.sorted_min = list()

    def push(self, val: int) -> None:
        self.stack.append(val)
        bisect.insort(self.sorted_min, val)  # O(log n) not O(1)
        # correct solution would be
        # self.sorted_min.append( val if not self.sorted_min else min(val, self.sorted_min[-1]) )

    def pop(self) -> None:
        val = self.stack.pop()
        self.sorted_min.remove(val)

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.sorted_min[0]
