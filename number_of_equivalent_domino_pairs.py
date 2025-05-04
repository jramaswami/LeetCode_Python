"""
LeetCode
1128. Number of Equivalent Domino Pairs
May 2025 Challenge
jramaswami
"""


import collections
import math
from typing import List


class Solution:
    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        freqs = collections.Counter(
            tuple(sorted(d)) for d in dominoes
        )
        return sum(math.comb(n, 2) for n in freqs.values())
            

def test_1():
    dominoes = [[1,2],[2,1],[3,4],[5,6]]
    expected = 1
    assert Solution().numEquivDominoPairs(dominoes) == expected
    

def test_2():
    dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]
    expected = 3
    assert Solution().numEquivDominoPairs(dominoes) == expected
