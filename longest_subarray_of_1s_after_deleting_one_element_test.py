"""
LeetCode
1493. Longest Subarray of 1's After Deleting One Element
July 2023 Challenge
jramaswami
Tests
"""


from longest_subarray_of_1s_after_deleting_one_element import Solution


def test_1():
    nums = [1,1,0,1]
    expected = 3
    assert Solution().longestSubarray(nums) == expected


def test_2():
    nums = [0,1,1,1,0,1,1,0,1]
    expected = 5
    assert Solution().longestSubarray(nums) == expected


def test_3():
    nums = [1,1,1]
    expected = 2
    assert Solution().longestSubarray(nums) == expected