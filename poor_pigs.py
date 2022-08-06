"""
LeetCode :: August 2022 Challenge :: Poor Pigs
jramaswami

REF: https://www.youtube.com/watch?v=9YSHcsprxh0
"""


import math


class Solution:

    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        # First, determine the number of testing periods.
        t = (minutesToTest // minutesToDie) + 1
        # You can create an n-dimensional matrix to find the bad bucket.
        # That means you need ceil(log_t(buckets)) pigs to find the bad bucket.
        return int(math.ceil(math.log(buckets, t)))


def test_1():
    buckets = 1000
    minutesToDie = 15
    minutesToTest = 60
    expected = 5
    assert Solution().poorPigs(buckets, minutesToDie, minutesToTest) == expected


def test_2():
    buckets = 4
    minutesToDie = 15
    minutesToTest = 15
    expected = 2
    assert Solution().poorPigs(buckets, minutesToDie, minutesToTest) == expected


def test_3():
    buckets = 4
    minutesToDie = 15
    minutesToTest = 30
    expected = 2
    assert Solution().poorPigs(buckets, minutesToDie, minutesToTest) == expected
