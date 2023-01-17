"""
LeetCode
996. Flip String to Monotone Increasing
January 2023 Challenge
jramaswami
"""


import itertools


class Solution:
    def minFlipsMonoIncr(self, S):
        suffix_sum = list(itertools.accumulate(reversed([int(i) for i in S])))[::-1]
        suffix_sum.append(0)

        def rec(i):
            if i >= len(S):
                return 0

            # If i is 1 then all the rest of the numbers must be one.
            # Cost is number of zeros
            slots = len(S) - i
            result = slots - suffix_sum[i]
            if S[i] == '0':
                # We can leave it zero.
                result = min(result, rec(i+1))
            else:
                # We can flip to zero.
                result = min(result, 1 + rec(i+1))
            return result

        return rec(0)


def test_1():
    S = "00110"
    assert Solution().minFlipsMonoIncr(S) == 1


def test_2():
    S = "010110"
    assert Solution().minFlipsMonoIncr(S) == 2


def test_3():
    S = "00011000"
    assert Solution().minFlipsMonoIncr(S) == 2