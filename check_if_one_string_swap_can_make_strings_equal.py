"""
LeetCode
1790. Check if One String Swap Can Make Strings Equal
February 2025 Challenge
jramaswami
"""


class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        difference_indexes = []
        for i, (a, b) in enumerate(zip(s1, s2)):
            if a != b:
                difference_indexes.append(i)
        if len(difference_indexes) == 0:
            return True
        if len(difference_indexes) == 2:
            i, j = difference_indexes
            return s1[i] == s2[j] and s1[j] == s2[i]
        return False
