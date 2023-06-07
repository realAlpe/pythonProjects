class Solution:
    """https://leetcode.com/problems/group-anagrams/"""

    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # Time limit exceeded.
        anagrams = []
        grouped_indices = set()
        for i in range(len(strs)):
            if i in grouped_indices:
                continue
            group = [strs[i]]
            for j in range(i + 1, len(strs)):
                if j not in grouped_indices and isAnagram(strs[i], strs[j]):
                    grouped_indices.add(j)
                    group.append(strs[j])
            anagrams.append(group)
        return anagrams


def isAnagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    for x in set(s):
        if s.count(x) != t.count(x):
            return False
    return True
