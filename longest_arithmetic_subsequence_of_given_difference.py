"""
LeetCode
1218. Longest Arithmetic Subsequence of Given Difference
July 2023 Challenge
jramaswami
"""


from typing import List


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        locations = dict()
        for i, n in enumerate(arr):
            if n in locations:
                locations[n].append(i)
            else:
                locations[n] = [i]

        dp = [1 for _ in arr]
        soln = 1
        for i, n in enumerate(arr):
            m = n + difference
            if m in locations:
                for j in locations[m]:
                    dp[j] = max(dp[j], dp[i] + 1)

        return max(dp)


def test_1():
    arr = [1,2,3,4]
    difference = 1
    expected = 4
    assert Solution().longestSubsequence(arr, difference) == expected


def test_2():
    arr = [1,3,5,7]
    difference = 1
    expected = 1
    assert Solution().longestSubsequence(arr, difference) == expected


def test_3():
    arr = [1,5,7,8,5,3,4,2,1]
    difference = -2
    expected = 4
    assert Solution().longestSubsequence(arr, difference) == expected


def test_4():
    "WA"
    arr = [-6,6,-8,0,7,-8,5,-7,10,-10]
    difference = -6
    expected = 2
    assert Solution().longestSubsequence(arr, difference) == expected