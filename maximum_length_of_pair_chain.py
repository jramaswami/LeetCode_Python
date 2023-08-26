"""
LeetCode
646. Maximum Length of Pair Chain
August 2023 Challenge
jramaswami
"""


from typing import List


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        dp = [1 for _ in pairs]
        for i, _ in enumerate(pairs):
            for j, _ in enumerate(pairs[i+1:], start = i + 1):
                if pairs[i][1] < pairs[j][0]:
                    dp[j] = max(dp[j], dp[i]+1)
        return max(dp)


def test_1():
    pairs = [[1,2],[2,3],[3,4]]
    expected = 2
    assert Solution().findLongestChain(pairs) == expected


def test_2():
    pairs = [[1,2],[2,3],[3,4]]
    expected = 2
    assert Solution().findLongestChain(pairs) == expected