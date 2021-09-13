"""
LeetCode :: September 2021 Challenge :: Maximum Number of Balloons
jramaswami
"""

from collections import Counter


class Solution:

    def maxNumberOfBalloons(self, text):
        ctr = Counter(text)
        letters = 'balon'
        required = [1, 1, 2, 2, 1]
        return min(ctr[c] // r for c, r in zip(letters, required))


def test_1():
    text = "nlaebolko"
    assert Solution().maxNumberOfBalloons(text) == 1


def test_2():
    text = "loonbalxballpoon"
    assert Solution().maxNumberOfBalloons(text) == 2


def test_3():
    text = 'leetcode'
    assert Solution().maxNumberOfBalloons(text) == 0


def test_4():
    text = ("balloon" * 100) + "ballon"
    assert Solution().maxNumberOfBalloons(text) == 100
