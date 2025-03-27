"""
LeetCode
2780. Minimum Index of a Valid Split
March 2025 Challenge
jramaswami
"""


from typing import List


class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        # Boyer-Moore
        majority = counter = 0
        for x in nums:
            if counter == 0:
                majority = x
            elif majority == x:
                counter += 1
            else:
                counter -= 1
        # Get frequency of majority element
        frequency = nums.count(majority)
        # Determine split point
        left_majority = 0
        for i, x in enumerate(nums):
            if x == majority:
                left_majority += 1
            left_length = i + 1
            right_length = len(nums) - left_length
            right_majority = frequency - left_majority
            left_minority = left_length - left_majority
            right_minority = right_length - right_majority
            if left_majority > left_minority and right_majority > right_minority:
                return i
        return -1


def test_1():
    nums = [1,2,2,2]
    expected = 2
    assert Solution().minimumIndex(nums) == expected


def test_2():
    nums = [2,1,3,1,1,1,7,1,2,1]
    expected = 4
    assert Solution().minimumIndex(nums) == expected


def test_3():
    nums = [3,3,3,3,7,2,2]
    expected = -1
    assert Solution().minimumIndex(nums) == expected


def test_4():
    "WA"
    nums = [1,1,1,2]
    expected = 0
    assert Solution().minimumIndex(nums) == expected