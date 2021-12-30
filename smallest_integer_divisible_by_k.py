"""
LeetCode :: December 2021 Challenge :: 1015. Smallest Integer Divisible by K
jramaswami
"""


class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:

        def find_digit(carry, k):
            "Return digit that results in 1 in the ones place."
            for d in range(10):
                summ = carry + (k * d)
                if summ % 10 == 1:
                    return summ // 10, d
            return carry, -1

        def all_ones(number):
            return all(c == '1' for c in str(number))


        carry = 0
        t = 0
        m = 1
        while not all_ones(k * t):
            carry, d = find_digit(carry, k)
            if d == -1:
                return -1
            t = t + (m * d)
            m *= 10

            # print(f"{k} * {t} = {k * t}")

        return len(str(k * t))


def test_1():
    k = 1
    assert Solution().smallestRepunitDivByK(k) == 1


def test_2():
    k = 2
    assert Solution().smallestRepunitDivByK(k) == -1


def test_3():
    k = 3
    assert Solution().smallestRepunitDivByK(k) == 3


def test_4():
    "TLE"
    k = 19927
    assert Solution().smallestRepunitDivByK(k) == 3
