"""
LeetCode :: Arrays Module :: Find Numbers with Even Number of Digits
jramaswami

Changing from log(n, 10) to log10(n) fixed the problem.  According to the
Python docs, log10(x) is more accurate than log(x, 10)?!?
"""


from math import log10


class Solution:
    def findNumbers(self, nums):
        return sum(int(log10(n) + 1) % 2 == 0 for n in nums)


def test_1():
    nums = [12,345,2,6,7896]
    assert Solution().findNumbers(nums) == 2


def test_2():
    nums = [555,901,482,1771]
    assert Solution().findNumbers(nums) == 1

def test_3():
    """WA"""
    nums = [1000]
    assert Solution().findNumbers(nums) == 1
