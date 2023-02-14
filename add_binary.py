"""
LeetCode
67. Add Binary
Feburary 2023 Challenge
jramaswami
"""


import itertools


class Solution:

    def addBinary(self, a, b):
        soln = []
        carry = 0
        for x, y in itertools.zip_longest(reversed(a), reversed(b), fillvalue='0'):
            t = int(x) + int(y) + carry
            carry, s = divmod(t, 2)
            soln.append(str(s))
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
