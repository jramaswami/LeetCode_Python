"""
LeetCode :: October 2022 Challenge :: 1335. Minimum Difficulty of a Job Schedule
jramaswami
"""


import math
import functools
from typing import *


class Solution:

    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:

        @functools.cache
        def rec(i, days_left, curr_max):
            "Recursive solution."
            # Prune.
            if days_left <= 0:
                return math.inf

            # Base case.
            if i >= len(jobDifficulty):
                if days_left == 1:
                    # print(acc)
                    return curr_max
                return math.inf

            # Compute.
            result = math.inf
            if i > 0:
                # We can partition before current job.
                result = min(
                    result,
                    curr_max + rec(i+1, days_left - 1, jobDifficulty[i])
                )
            # We can keep current job in current partition.
            result = min(
                result,
                rec(i+1, days_left, max(curr_max, jobDifficulty[i]))
            )
            return result

        soln = rec(0, d, -math.inf)
        return -1 if soln == math.inf else soln


def test_1():
    jobDifficulty = [6,5,4,3,2,1]
    d = 2
    expected = 7
    assert Solution().minDifficulty(jobDifficulty, d) == expected


def test_2():
    jobDifficulty = [9,9,9]
    d = 4
    expected = -1
    assert Solution().minDifficulty(jobDifficulty, d) == expected


def test_3():
    jobDifficulty = [1,1,1]
    d = 3
    expected = 3
    assert Solution().minDifficulty(jobDifficulty, d) == expected