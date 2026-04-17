"""
LeetCode
3761. Minimum Absolute Distance Between Mirror Pairs
LeetCode
jramaswami
"""


import collections
from typing import List


class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        INF = pow(10, 10)
        soln = INF
        locations = collections.defaultdict(list)
        for j, n in enumerate(nums):
            m = int(''.join(reversed(str(n))))
            if n in locations:
                i = locations[n][-1]
                soln = min(soln, j - i)
            locations[m].append(j)
        return soln if soln < INF else -1