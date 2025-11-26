"""
LeetCode
1018. Binary Prefix Divisible By 5
November 2025 Challenge
jramaswami
"""


from typing import List


class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        soln = []
        acc = 0
        for n in nums:
            acc *= 2
            acc += n
            acc %= 5
            soln.append(acc == 0)
        return soln