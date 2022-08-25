"""
LeetCode :: August 2022 Challenge :: 383. Ransom Note
jramaswami
"""


import collections
import string


class Solution:
    def canConstruct(self, ransom_note: str, magazine: str) -> bool:
        ransom_freqs = collections.Counter(ransom_note)
        magazine_freqs = collections.Counter(magazine)
        for char in string.ascii_lowercase:
            if magazine_freqs[char] < ransom_freqs[char]:
                return False
        return True