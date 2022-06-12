"""
LeetCode :: June 2022 Challenge :: Maximum Erasure Value
jramaswami
"""


import collections
import math


class Solution:
    def maximumUniqueSubarray(self, nums):
        window = collections.deque()
        curr_score = 0
        max_score = -math.inf
        freqs = collections.defaultdict(int)
        for n in nums:
            window.append(n)
            freqs[n] += 1
            curr_score += n
            while freqs[n] > 1:
                freqs[window[0]] -= 1
                curr_score -= window[0]
                window.popleft()
            max_score = max(max_score, curr_score)
        return max_score


def test_1():
    nums = [4,2,4,5,6]
    expected = 17
    assert Solution().maximumUniqueSubarray(nums) == expected


def test_2():
    nums = [5,2,1,2,5,2,1,2,5]
    expected = 8
    assert Solution().maximumUniqueSubarray(nums) == expected


def test_3():
    nums = [4, 4, 2, 3, 2, 4, 2, 3, 5, 5, 3, 2, 2, 4, 5, 3, 2, 4, 3, 4]
    #          -------(9)
    #                -------(9)
    #                      -----------(14)
    #                                 --------(10)
    #                                          -----------(14)
    #                                                      ---------(9)
    expected = 14
    assert Solution().maximumUniqueSubarray(nums) == expected


def test_4():
    nums = [19, 11, 2, 15, 7, 11, 3, 12, 16, 20, 19, 1, 19, 3, 14, 9, 8, 16,
            13, 14, 15, 15, 10, 10, 16, 11, 18, 3, 9, 17, 7, 9, 18, 15, 18,
            6, 16, 18, 6, 4, 11, 10, 16, 8, 1, 9, 15, 14, 5, 1]
    expected = 117
    assert Solution().maximumUniqueSubarray(nums) == expected


def test_5():
    nums = [1 for _ in range(pow(10,5))]
    expected = 1
    assert Solution().maximumUniqueSubarray(nums) == expected
