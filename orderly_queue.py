"""
LeetCode :: September 2021 Challenge :: Orderly Queue
jramaswami

Thank You Larry!
"""


from collections import deque


class Solution:

    def orderlyQueue(self, S, k):
        if k >= 2:
            return "".join(sorted(S))

        min_s = S
        S0 = deque(S)
        for _ in range(len(S0)):
            S0.rotate(-1)
            S = "".join(S0)
            min_s = min(min_s, S)
        return min_s


def test_1():
    S = "cba"
    k = 1
    assert Solution().orderlyQueue(S, k) == "acb"


def test_2():
    S = "baaca"
    k = 3
    assert Solution().orderlyQueue(S, k) == "aaabc"


def test_3():
    S = "udvixligwqoltasj"
    k = 3
    assert Solution().orderlyQueue(S, k) == "adgiijlloqstuvwx"
