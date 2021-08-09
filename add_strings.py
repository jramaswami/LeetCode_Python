"""
LeetCode :: August 2021 Challenge :: Add Strings
jramaswami
"""


from itertools import zip_longest
from functools import reduce
from operator import add


class Number:
    def __init__(self, n=None):
        self.negative = False
        self.digits = []
        if n is not None:
            if n[0] == '-':
                self.negative = True
                self.digits = list(reversed(n[1:]))
            else:
                self.digits = list(reversed(n))

    def __add__(self, other):
        """
        This is incomplete!  It does not handle negative numbers because the
        problem did not require it.
        """
        soln = []
        carry = 0
        for a, b in zip_longest(self.digits, other.digits, fillvalue='0'):
            ds = carry + int(a) + int(b)
            k = ds % 10
            carry = ds // 10
            soln.append(str(k))
        if carry > 0:
            soln.append(str(carry))
        result = Number()
        result.digits = soln
        return result

    def __mul__(self, other):
        addends = []
        for i, a in enumerate(self.digits):
            addend = []
            for _ in range(i):
                addend.append('0')
            carry = 0
            for b in other.digits:
                ds = carry + (int(a) * int(b))
                k = ds % 10
                carry = ds // 10
                addend.append(k)

            if carry > 0:
                addend.append(str(carry))

            n = Number()
            n.digits = addend
            addends.append(n)

        result = reduce(add, addends, Number('0'))
        if self.negative != other.negative:
            result.negative = True
        return result

    def __repr__(self):
        if self.negative:
            return "Number(-{})".format("".join(reversed(self.digits)))
        else:
            return "Number({})".format("".join(reversed(self.digits)))

    def __str__(self):
        if self.negative:
            return "-{}".format("".join(reversed(self.digits)))
        else:
            return "{}".format("".join(reversed(self.digits)))

    def __eq__(self, other):
        return self.negative == other.negative and self.digits == other.digits


class Solution:
    def addStrings(self, num1, num2):
        return str(Number(num1) + Number(num2))


def test_1():
    num1 = "11"
    num2 = "123"
    expected = "134"
    result = Solution().addStrings(num1, num2)
    assert result == expected

def test_2():
    num1 = "456"
    num2 = "77"
    expected = "533"
    result = Solution().addStrings(num1, num2)
    assert result == expected

def test_3():
    num1 = "0"
    num2 = "0"
    expected = "0"
    result = Solution().addStrings(num1, num2)
    assert result == expected
