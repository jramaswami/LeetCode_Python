"""
LeetCode
3314. Construct the Minimum Bitwise Array I
January 2026 Challenge
jramawami
"""


from typing import List


class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        def f(x):
            for n in range(0, x):
                if n | (n+1) == x:
                    return n
            return -1

        return [f(x) for x in nums]