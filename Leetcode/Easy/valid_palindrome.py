class Solution:
    """https://leetcode.com/problems/valid-palindrome/"""

    def isPalindrome(self, s: str) -> bool:
        formatted = [char.lower() for char in s if char.isalnum()]
        n = len(formatted)
        for i in range(n // 2):
            if formatted[i] != formatted[n - 1 - i]:
                return False
        return True
