"""
LeetCode :: 72. Edit Distance
jramaswami
"""


class Solution:

    def minDistance(self, word1, word2):

        # Boundary cases
        if word1 == "":
            return len(word2)
        if word2 == "":
            return len(word1)

        # dp[word2][word1]
        dp = [[0 for _ in range(len(word1) + 1)] for _ in range(len(word2) + 1)]

        # Init
        dp[0] = list(range(len(word1) + 1))
        for r in range(len(word2) + 1):
            dp[r][0] = r

        # Compute
        for c in range(1, len(word1) + 1):
            a = word1[c-1]
            for r in range(1, len(word2) + 1):
                b = word2[r-1]
                if a == b:
                    # Match
                    dp[r][c] = dp[r-1][c-1]
                else:
                    # Substitution
                    dp[r][c] = 1 + min(
                        dp[r-1][c-1], # Substitution
                        dp[r][c-1],   # Insertion
                        dp[r-1][c]    # Deletion
                    )
        return dp[-1][-1]


def test_1():
    word1 = "horse"
    word2 = "ros"
    expected = 3
    assert Solution().minDistance(word1, word2) == expected


def test_2():
    word1 = "intention"
    word2 = "execution"
    expected = 5
    assert Solution().minDistance(word1, word2) == expected


def test_3():
    "RTE"
    word1 = ""
    word2 = ""
    expected = 0
    assert Solution().minDistance(word1, word2) == expected


def test_4():
    "WA"
    word1 = "a"
    word2 = "b"
    expected = 1
    assert Solution().minDistance(word1, word2) == expected
