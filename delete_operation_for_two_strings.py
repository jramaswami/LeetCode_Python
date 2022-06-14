"""
Leet Code :: May 2021 Challenge :: Delete Operation for Two Strings
jramaswami
"""


import functools


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        @functools.cache
        def solve(i, j):
            if i >= len(word1):
                return len(word2) - j
            if j >= len(word2):
                return len(word1) - i

            if word1[i] == word2[j]:
                return solve(i+1, j+1)
            return min(
                1 + solve(i+1, j),
                1 + solve(i, j+1)
            )

        return solve(0, 0)



def test_1():
    word1 = "sea"
    word2 = "eat"
    assert Solution().minDistance(word1, word2) == 2


def test_2():
    word1 = "leetcode"
    word2 = "etco"
    assert Solution().minDistance(word1, word2) == 4


def test_3():
    """WA"""
    word1 = "sea"
    word2 = "ate"
    assert Solution().minDistance(word1, word2) == 4


def test_4():
    word1 = "yqeoiryeuyeiuoadfuiaydfuiyasdfiouyfduiyaiusodioasudfyoiauyf"
    word2 = "qwoieruqowreuoqpwreuoiqwrepqoweurpoaufpouafpoiausfoiu"
    assert Solution().minDistance(word1, word2) == 62
