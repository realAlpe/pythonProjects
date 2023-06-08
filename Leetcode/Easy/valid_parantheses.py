class Solution:
    """https://leetcode.com/problems/valid-parentheses/"""

    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in r"({[":
                stack.append(char)
            else:  # char in r")}]"
                if len(stack) == 0:
                    return False
                ob = stack.pop()  # opening bracket, either (, [ or {
                if char == ")" and ob != "(":
                    return False
                if char == "]" and ob != "[":
                    return False
                if char == "}" and ob != "{":
                    return False
        return len(stack) == 0
