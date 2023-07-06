"""
LeetCode
209. Minimum Size Subarray Sum
July 2023 Challenge
jramaswami
Tests
"""


from minimum_size_subarray_sum import Solution


def test_1():
    target = 7
    nums = [2,3,1,2,4,3]
    expected = 2
    assert Solution().minSubArrayLen(target, nums) == expected


def test_2():
    target = 4
    nums = [1,4,4]
    expected = 1
    assert Solution().minSubArrayLen(target, nums) == expected


def test_3():
    target = 11
    nums = [1,1,1,1,1,1,1,1]
    expected = 0
    assert Solution().minSubArrayLen(target, nums) == expected