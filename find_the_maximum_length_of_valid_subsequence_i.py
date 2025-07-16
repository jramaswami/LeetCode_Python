"""
LeetCode
3201. Find the Maximum Length of Valid Subsequence I
July 2025 Challenge
jramaswami
"""


from typing import List


class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        parity = [n % 2 for n in nums]

        def alternating_parity(i, p):
            if i >= len(parity):
                return 0

            if parity[i] == p:
                return 1 + alternating_parity(i+1, (p+1)%2)
            return 0 + alternating_parity(i+1, p)

        odds = sum(parity)
        evens = len(parity) - odds
        alternating_odd = alternating_parity(0, 1)
        alternating_even = alternating_parity(0, 0)
        return max(odds, evens, alternating_odd, alternating_even)