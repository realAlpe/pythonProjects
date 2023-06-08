class Solution:
    """https://leetcode.com/problems/generate-parentheses/"""

    def generateParenthesis(self, n: int) -> list[str]:
        if n == 1:
            return ["()"]
        previous = self.generateParenthesis(n - 1)
        solution = set()
        for sub_solution in previous:
            solution.update(extend_parentheses(sub_solution))
        print(f"{n=}, {solution=}")
        return list(solution)


def extend_parentheses(s: str) -> set[str]:
    return {
        s[:i] + "(" + s[i:j] + ")" + s[j:]
        for i in range(len(s) + 1)
        for j in range(i, len(s) + 1)
    }
