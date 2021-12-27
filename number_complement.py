"""
LeetCode :: December 2021 Challenge :: 476. Number Complement
jramaswami
"""


class Solution:
    def findComplement(self, num: int) -> int:
        soln = 0
        bit = 0
        while num:
            if num & 1:
                pass
            else:
                soln |= (1 << bit)
            num = num >> 1
            bit += 1
        return soln


def test_1():
    assert Solution().findComplement(5) == 2


def test_2():
    assert Solution().findComplement(1) == 0
