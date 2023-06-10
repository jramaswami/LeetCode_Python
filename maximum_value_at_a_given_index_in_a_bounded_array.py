"""
LeetCode
1802. Maximum Value at a Given Index in a Bounded Array
June 2023
jramaswami
"""


class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        # Edge cases:
        if n == 1:
            return maxSum
        if n >= maxSum:
            return 1

        # Compute how many slots there are to fill to the left and
        # right of the selected index.
        left_fill = index
        right_fill = n - index - 1

        # Make all numbers 1.
        maxSum -= n

        # Make the selected index 2.
        soln = 2
        maxSum -= 1

        # Loop filling each side up so that difference between items is always
        # just 1.
        curr_left = min(1, left_fill)
        curr_right = min(1, right_fill)
        while maxSum > 0:
            curr_total_fill = curr_left + curr_right + 1
            maxSum -= curr_total_fill
            if maxSum >= 0:
                soln += 1
            curr_left = min(curr_left + 1, left_fill)
            curr_right = min(curr_right + 1, right_fill)
        return soln


def test_1():
    n = 4
    index = 2
    maxSum = 6
    expected = 2
    assert Solution().maxValue(n, index, maxSum) == expected


def test_2():
    n = 6
    index = 1
    maxSum = 10
    expected = 3
    assert Solution().maxValue(n, index, maxSum) == expected


def test_3():
    "TLE"
    n = 3
    index = 0
    maxSum = 815094800
    expected = 271698267
    assert Solution().maxValue(n, index, maxSum) == expected