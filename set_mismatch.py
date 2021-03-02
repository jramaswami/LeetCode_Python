"""
LeetCode :: March 2021 Challenge :: Set Mismatch
jramaswami
"""
from typing import *


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        N = len(nums)
        # expected_sum = N(N + 1) / 2
        # real_sum + missing - duplicate = expected_sum
        # RS + m - d = ES
        # m - d = ES - RS
        # m - d = A
        ES = (N * (N + 1)) // 2
        ES = sum(range(1, N+1))
        RS = sum(nums)
        A = ES - RS

        # expected_square_sum = N(N+1)(2N+1) / 6
        # real_square_sum + missing^2 - duplicate^2 = expected_square_sum
        # RSS + m^2 - d^2 = ESS
        # m^2 - d^2 = ESS - RSS
        # m^2 - d^2 = B
        ESS = (N * (N + 1) * ((2 * N) + 1)) // 6
        ESS = sum(k * k for k in range(1, N+1))
        RSS = sum(n * n for n in nums)
        B = ESS - RSS

        # m - d = A
        # m = A + d

        # m^2 - d^2 = B
        # (A + d)^2 - d^2 = B
        # A^2 + 2Ad + d^2 - d^2 = B
        # A^2 + 2Ad = B
        # 2Ad = B - A^2
        # d = (B - A^2) / 2A
        duplicate = (B - (A*A)) // (2 * A)

        # m - d = A
        # m = A + d
        missing = A + duplicate

        return [duplicate, missing]


def test_1():
    assert Solution().findErrorNums([1, 2, 2, 4]) == [2, 3]

def test_2():
    assert Solution().findErrorNums([1, 1]) == [1, 2]
