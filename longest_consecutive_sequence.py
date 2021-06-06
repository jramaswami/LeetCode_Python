"""
LeetCode :: June 2021 Challenge :: Longest Consecutive Sequence
jramaswami
"""


from typing import *


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums0 = set(nums)
        best = {}

        def get_longest_sequence(n):
            if n in best:
                return best[n]
            if n not in nums0:
                return 0
            best[n] = 1 + get_longest_sequence(n + 1)
            return best[n]

        soln = 0
        for n in nums0:
            soln = max(soln, get_longest_sequence(n))
        return soln


def test_1():
    nums = [100,4,200,1,3,2]
    assert Solution().longestConsecutive(nums) == 4


def test_2():
    nums = [0,3,7,2,5,8,4,6,0,1]
    assert Solution().longestConsecutive(nums) == 9


def test_3():
    """WA"""
    nums = [9,1,-3,2,4,8,3,-1,6,-2,-4,7]
    assert Solution().longestConsecutive(nums) == 4
