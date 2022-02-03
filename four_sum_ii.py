"""
LeetCode :: February 2022 Challenge :: 454. 4Sum II
jramswami
"""


import collections


class Solution:

    def fourSumCount(self, nums1, nums2, nums3, nums4):
        freqs = collections.defaultdict(int)
        for a in nums1:
            for b in nums2:
                freqs[a+b] += 1

        soln = 0
        for a in nums3:
            for b in nums4:
                soln += freqs[-(a+b)]
        return soln


def test_1():
    nums1 = [1,2]
    nums2 = [-2,-1]
    nums3 = [-1,2]
    nums4 = [0,2]
    expected = 2
    assert Solution().fourSumCount(nums1, nums2, nums3, nums4) == expected


def test_2():
    nums1 = [0]
    nums2 = [0]
    nums3 = [0]
    nums4 = [0]
    expected = 1
    assert Solution().fourSumCount(nums1, nums2, nums3, nums4) == expected
