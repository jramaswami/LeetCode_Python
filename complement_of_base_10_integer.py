"""
LeetCode :: January 2022 Challenge :: 1009. Complement of Base 10 Integer
jramaswami
"""


class Solution:
    def bitwiseComplement(self, num: int) -> int:
        # Special case:
        if num == 0:
            return 1
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
    assert Solution().bitwiseComplement(5) == 2


def test_2():
    assert Solution().bitwiseComplement(1) == 0


def test_3():
    "WA"
    assert Solution().bitwiseComplement(0) == 1

