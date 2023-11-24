"""
LeetCode
1561. Maximum Number of Coins You Can Get
November 2023 Challenge
jramaswami
"""


from typing import List
import collections


class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles0 = collections.deque(sorted(piles))
        soln = 0
        while piles0:
            piles0.pop()  # Alice
            soln += piles0.pop()   # Me
            piles0.popleft()  # Bob
        return soln