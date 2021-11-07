"""
LeetCode :: November 2021 Challenge :: 43. Multiply Strings
jramaswami
"""


from typing import *
from itertools import zip_longest


class NumberString:

    @staticmethod
    def from_string(S):
        reversed_digits = [int(c) for c in S][::-1]
        return NumberString(reversed_digits)

    @staticmethod
    def from_integer(N):
        return NumberString.from_string(str(N))

    def __init__(self, reversed_digits):
        self.reversed_digits = reversed_digits

    def __add__(self, other):
        carry = 0
        new_digits = []
        for a, b in zip_longest(self.reversed_digits, other.reversed_digits, fillvalue=0):
            t = a + b + carry
            carry, d = divmod(t, 10)
            new_digits.append(d)
        if carry:
            new_digits.append(carry)
        return NumberString(new_digits)

    def __mul__(self, other):
        padding = 0
        addends = []
        result = NumberString.from_integer(0)
        for d in self.reversed_digits:
            new_number = []
            carry = 0
            # Add padding
            for _ in range(padding):
                new_number.append(0)
            # Increment padding for next digit.
            padding += 1
            # Multiply
            for a in other.reversed_digits:
                t = (a * d) + carry
                carry, r = divmod(t, 10)
                new_number.append(r)
            if carry:
                new_number.append(carry)
            # Add digit product to the result
            result = result + NumberString(new_number)
        return result

    def __str__(self):
        # Remove leading zeros.
        while len(self.reversed_digits) > 1 and self.reversed_digits[-1] == 0:
            self.reversed_digits.pop()

        return "".join([str(d) for d in self.reversed_digits][::-1])

    def __int__(self):
        N = 0
        place = 1
        for d in self.reversed_digits:
            N += (place * d)
            place *= 10
        return N


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(NumberString.from_string(num1) * NumberString.from_string(num2))


#
# Testing
#
import random


def test_to_int():
    for _ in range(1000):
        a = random.randint(0, 1000)
        A = NumberString.from_integer(a)
        assert int(A) == a


def test_addition():
    for _ in range(1000):
        a = random.randint(0, 10000)
        b = random.randint(0, 10000)
        expected = a + b
        A = NumberString.from_integer(a)
        B = NumberString.from_integer(b)
        assert int(A + B) == a + b


def test_multiplication():
    for _ in range(1000):
        a = random.randint(0, 10000)
        b = random.randint(0, 10000)
        expected = a + b
        A = NumberString.from_integer(a)
        B = NumberString.from_integer(b)
        assert int(A * B) == a * b


def test_1():
    num1 = "2"
    num2 = "3"
    expected = "6"
    assert Solution().multiply(num1, num2) == expected


def test_2():
    num1 = "123"
    num2 = "456"
    expected = "56088"
    assert Solution().multiply(num1, num2) == expected


def test_3():
    num1 = "123"
    num2 = "0"
    expected = "0"
    assert Solution().multiply(num1, num2) == expected


def test_random():
    for _ in range(1000):
        a = random.randint(0, 10000)
        b = random.randint(0, 10000)
        expected = str(a * b)
        assert Solution().multiply(str(a), str(b)) == expected