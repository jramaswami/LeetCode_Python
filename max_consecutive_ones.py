"""
LeetCode :: 485. Max Consecutive Ones
jramaswami
"""


class Solution:
    def findMaxConsecutiveOnes(self, nums):
        soln = curr_sum = 0
        for i, n in enumerate(nums):
            curr_sum = (curr_sum + n) * n
            soln = max(soln, curr_sum)
        return soln


def test_1():
    assert Solution().findMaxConsecutiveOnes([1,1,0,1,1,1]) == 3


def test_2():
    assert Solution().findMaxConsecutiveOnes([1,0,1,1,0,1]) == 2
