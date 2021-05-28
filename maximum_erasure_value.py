"""
LeetCode :: May 2021 Challenge :: Maximum Erasure Value
jramaswami
"""


from typing import *
from collections import deque, defaultdict


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        frequency = defaultdict(int)
        subarray = deque()
        curr_sum = 0
        best_sum = 0
        for n in nums:
            # Add n to the subarray
            subarray.append(n)
            frequency[n] += 1
            curr_sum += n
            # If the frequency of n > 1, then remove items until it is.
            while frequency[n] > 1:
                k = subarray.popleft()
                frequency[k] -= 1
                curr_sum -= k
            # Remember best sum
            best_sum = max(curr_sum, best_sum)
        return best_sum



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