"""
LeetCode :: June 2021 Challenge :: Number of Subarrays with Bounded Maximum
jramaswami
"""

from collections import deque


class Solution:
    """
    We are given an array nums of positive integers, and two positive integers
    left and right (left <= right).

    Return the number of (contiguous, non-empty) subarrays such that the value
    of the maximum array element in that subarray is at least left and at most
    right.
    """
    def numSubarrayBoundedMax(self, nums, left, right):
        """Solve problem."""
        values_gte_left = deque((x, i) for i, x in enumerate(nums) if x >= left)
        values_gt_right = deque((x, i) for i, x in enumerate(nums) if x > right)
        values_gt_right.append((None, len(nums)))
        values_gte_left.append((None, len(nums)))
        soln = 0
        for i, n in enumerate(nums):

            while values_gte_left and values_gte_left[0][1] < i:
                values_gte_left.popleft()

            while values_gt_right and values_gt_right[0][1] <= i:
                values_gt_right.popleft()

            if n <= right:
                # Subarrays starting with me that have left <= max <= right
                # begin where the next value >= left is and end where then
                # next value > right is.
                if values_gt_right[0][1] > values_gte_left[0][1]:
                    delta = values_gt_right[0][1] - values_gte_left[0][1]
                    soln += delta
        return soln


def test_1():
    """Sample test 1"""
    nums = [2, 1, 4, 3]
    left = 2
    right = 3
    assert Solution().numSubarrayBoundedMax(nums, left, right) == 3


def test_2():
    nums = [17, 7, 18, 11, 5, 12, 1, 2, 20, 14, 16, 8, 19, 6, 8, 14, 15, 11, 18, 11]
    left = 10
    right = 15
    assert Solution().numSubarrayBoundedMax(nums, left, right) == 25


def test_3():
    """RTE"""
    nums = [16, 69, 88, 85, 79, 87, 37, 33, 39, 34]
    left = 55
    right = 57
    assert Solution().numSubarrayBoundedMax(nums, left, right) == 25
