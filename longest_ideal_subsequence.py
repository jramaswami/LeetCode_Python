"""
LeetCode
2370. Longest Ideal Subsequence
April 2024 Challenge
jramaswami
"""


class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        ord_a = ord('a')
        t = [ord(c) - ord_a for c in s]
        dp = [0 for _ in range(26)]
        for x in t:
            left = max(0, x - k)
            right = min(25, x + k)

            longest = dp[x]
            for y in range(left, right+1):
                longest = max(longest, 1 + dp[y])
            dp[x] = longest
        return max(dp)


def test_1():
    s = "acfgbd"
    k = 2
    expected = 4
    result = Solution().longestIdealString(s,k)
    assert result == expected


def test_2():
    s = "abcd"
    k = 3
    expected = 4
    result = Solution().longestIdealString(s,k)
    assert result == expected