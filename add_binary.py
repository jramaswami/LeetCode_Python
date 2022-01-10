"""
LeetCode :: January 2022 Challenge :: 67. Add Binary
jramaswami
"""


import itertools


class Solution:

    def addBinary(self, a, b):
        soln = []
        carry = 0
        for x, y in itertools.zip_longest(reversed(a), reversed(b), fillvalue='0'):
            p = int(x)
            q = int(y)
            t = p + q + carry
            carry = 0
            if t == 3:
                t = 1
                carry = 1
            elif t == 2:
                t = 0
                carry = 1
            soln.append(str(t))
        if carry:
            soln.append(str(carry))
        return "".join(reversed(soln))


def test_1():
    a = "11"
    b = "1"
    expected = "100"
    assert Solution().addBinary(a, b) == expected


def test_2():
    a = "1010"
    b = "1011"
    expected = "10101"
    assert Solution().addBinary(a, b) == expected
