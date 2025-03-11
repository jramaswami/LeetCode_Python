"""
LeetCode
1358. Number of Substrings Containing All Three Characters
March 2025 Challenge
jramaswami
"""


class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        soln = 0
        l = 0
        freqs = {'a': 0, 'b': 0, 'c': 0}
        for r, _ in enumerate(s):
            freqs[s[r]] += 1
            while all(t > 0 for t in freqs.values()):
                soln += (len(s) - r)
                freqs[s[l]] -= 1
                l += 1
        return soln
