"""
LeetCode
859. Buddy Strings
July 2023 Challenge
jramaswami
"""


import collections


class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        letter_freqs = collections.defaultdict(int)
        difference_indexes = []
        for i, (a, b) in enumerate(zip(s, goal)):
            letter_freqs[a] += 1
            if a != b:
                difference_indexes.append(i)

        if len(difference_indexes) == 0:
            return any(f > 1 for f in letter_freqs.values())
        if len(difference_indexes) == 2:
            i, j = difference_indexes
            return s[i] == goal[j] and s[j] == goal[i]
        return False