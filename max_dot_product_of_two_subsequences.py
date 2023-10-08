"""
LeetCode
1458. Max Dot Product of Two Subsequences
October 2023 Challenge
jramaswami
"""


from typing import List
import math


class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[-math.inf for _ in range(len(nums2)+1)] for _ in range(len(nums1)+1)]
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                dp[i+1][j] = max(dp[i][j], dp[i+1][j])
                dp[i][j+1] = max(dp[i][j], dp[i][j+1])
                dp[i+1][j+1] = max(
                    dp[i][j],
                    dp[i+1][j+1],
                    max(0, dp[i][j]) + (nums1[i] * nums2[j])
                )

        return max(max(row) for row in dp)



def test_1():
    nums1 = [2,1,-2,5]
    nums2 = [3,0,-6]
    expected = 18
    assert Solution().maxDotProduct(nums1, nums2) == expected


def test_2():
    nums1 = [3,-2]
    nums2 = [2,-6,7]
    expected = 21
    assert Solution().maxDotProduct(nums1, nums2) == expected


def test_3():
    nums1 = [-1,-1]
    nums2 = [1,1]
    expected = -1
    assert Solution().maxDotProduct(nums1, nums2) == expected