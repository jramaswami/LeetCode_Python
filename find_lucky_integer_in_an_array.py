"""
LeetCode
1394. Find Lucky Integer in an Array
July 2025 Challenge
jramaswami
"""


import collections
from typing import List


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        soln = -1
        freqs = collections.Counter(arr)
        for n in sorted(freqs):
            if n == freqs[n]:
                soln = n
        return soln