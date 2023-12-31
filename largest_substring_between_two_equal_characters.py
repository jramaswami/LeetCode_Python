"""
LeetCode
1624. Largest Substring Between Two Equal Characters
December 2023 Challenge
jramaswami
"""


import collections


class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        posns = collections.defaultdict(list)
        for i, c in enumerate(s):
            posns[c].append(i)

        soln = -1
        for c in posns:
            if len(posns[c]) > 1:
                soln = max(soln, posns[c][-1] - posns[c][0] - 1)
        return soln