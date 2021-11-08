"""
LeetCode :: November 2021 Challenge :: 96. Unique Binary Search Trees
jramaswami


The number of Unique BST's is the Catalan number:

C(n) = (2n choose n) / (n + 1) = (2n)! / [(n+1)! * n!]
"""


class Solution:

    def __init__(self):
        # Cache factorials up to 2 * MAXN.
        MAXN = 19
        self.factorials = [1, 1]
        for k in range(2, (2 * MAXN) + 1):
            self.factorials.append(k * self.factorials[-1])

    def numTrees(self, n):
        numerator = self.factorials[2 * n]
        denominator = self.factorials[n + 1] * self.factorials[n]
        return numerator // denominator


def test_1():
    assert Solution().numTrees(1) == 1


def test_2():
    assert Solution().numTrees(3) == 5