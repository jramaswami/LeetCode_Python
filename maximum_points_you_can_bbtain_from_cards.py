"""
Leet Code :: May 2021 Challenge :: Maximum Points You Can Obtain from Cards
jramaswami
"""
from typing import *
from itertools import accumulate


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        left_prefix = [0] + list(accumulate(cardPoints[:k]))
        right_prefix = list(accumulate(cardPoints[-k:][::-1]))[::-1]
        right_prefix.append(0)
        return max(a + b for a, b in zip(left_prefix, right_prefix))



def test_1():
    cardPoints = [1,2,3,4,5,6,1]
    k = 3
    assert Solution().maxScore(cardPoints, k) == 12


def test_2():
    cardPoints = [2,2,2]
    k = 2
    assert Solution().maxScore(cardPoints, k) == 4


def test_3():
    cardPoints = [9,7,7,9,7,7,9]
    k = 7
    assert Solution().maxScore(cardPoints, k) == 55


def test_4():
    cardPoints = [1,1000,1]
    k = 1
    assert Solution().maxScore(cardPoints, k) == 1


def test_5():
    cardPoints = [1,79,80,1,1,1,200,1]
    k = 3
    assert Solution().maxScore(cardPoints, k) == 202


def test_6():
    cardPoints = [359, 723, 910, 103, 923, 670, 693, 4, 204, 484, 428, 422, 358, 246, 615, 311, 347, 541, 123, 422, 343, 578, 586, 496, 896, 120, 93, 998, 479, 896, 986, 470, 463, 855, 249, 791, 126, 141, 387, 545, 815, 310, 527, 272, 892, 223, 6, 382, 321, 409]
    k = 25
    assert Solution().maxScore(cardPoints, k) == 12625


def test_7():
    cardPoints = [359, 723, 910, 103, 923, 670, 693, 4, 204, 484, 428, 422, 358, 246, 615, 311, 347, 541, 123, 422, 343, 578, 586, 496, 896, 120, 93, 998, 479, 896, 986, 470, 463, 855, 249, 791, 126, 141, 387, 545, 815, 310, 527, 272, 892, 223, 6, 382, 321, 409]
    k = 4
    assert Solution().maxScore(cardPoints, k) == 2401

