"""
LeetCode :: May 2022 Challenge :: Missing Number
jramaswami
"""


class Solution:
    def missingNumber(self, nums):
        N = len(nums)
        S = (N * (N + 1)) // 2
        return S - sum(nums)


def test_1():
    assert Solution().missingNumber([3,0,1]) == 2

def test_2():
    assert Solution().missingNumber([0,1]) == 2

def test_3():
    assert Solution().missingNumber([9,6,4,2,3,5,7,0,1]) == 8

def test_4():
    assert Solution().missingNumber([0]) == 1
