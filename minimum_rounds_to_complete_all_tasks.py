"""
LeetCode
2244. Minimum Rounds to Complete All Tasks
January 2023 Challenge
jramaswami
"""


from typing import *
import collections
import math


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        freqs = collections.Counter(tasks)
        soln = 0
        for task, freq in freqs.items():
            if freq < 3:
                if freq == 1:
                    return -1
                soln += 1
            else:
                soln += int(math.ceil(freq / 3))
        return soln


def test_1():
    tasks = [2,2,3,3,2,4,4,4,4,4]
    expected = 4
    assert Solution().minimumRounds(tasks) == expected


def test_2():
    tasks = [2,3,3]
    expected = -1
    assert Solution().minimumRounds(tasks) == expected
