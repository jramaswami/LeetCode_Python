"""
LeetCode
1002. Find Common Characters
June 2024 Challenge
jramaswami
"""


import collections
import string


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        soln = []
        freqs = [collections.Counter(w) for w in words]
        for char in string.ascii_lowercase:
            min_freq = min(f[char] for f in freqs)
            for _ in range(min_freq):
                soln.append(char)
        return soln   
