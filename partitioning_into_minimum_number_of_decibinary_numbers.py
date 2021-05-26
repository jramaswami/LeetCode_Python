"""
LeetCode :: May 2021 Challenge :: Partitioning Into Minimum Number Of Deci-Binary Numbers
jramaswami
"""


from typing import *


class Solution:
    def minPartitions(self, n: str) -> int:
        return max(int(i) for i in n)



def test_1():
    n = "32"
    assert Solution().minPartitions(n) == 3


def test_2():
    n = "82734"
    assert Solution().minPartitions(n) == 8


def test_3():
    n = "27346209830709182346"
    assert Solution().minPartitions(n) == 9