class Solution:
    """https://leetcode.com/problems/group-anagrams/"""

    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        h = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word in h:
                h[sorted_word].append(word)
            else:
                h[sorted_word] = [word]
        return list(h.values())
