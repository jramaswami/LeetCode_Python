"""
LeetCode :: December 2021 Challenge :: 902. Numbers At Most N Given Digit Set
jramaswami
"""


class Solution:
    def atMostNGivenDigitSet(self, digits, limit):
        digits = [int(d) for d in digits]
        powers = [1]
        powers_prefix = [0]      # Cannot make a zero-digit number.
        limit0 = [int(i) for i in str(limit)]
        while len(powers) < len(limit0):
            powers.append(powers[-1] * len(digits))
            powers_prefix.append(powers_prefix[-1] + powers[-1])

        # Count numbers with less digits than the limit.
        soln = powers_prefix[len(limit0) - 1]

        # Count numbers with same number of digits.
        for offset, k in enumerate(limit0):
            # We are working on the ith placed digit (indexed from 1).
            i = len(limit0) - offset
            # Count the number of digits less than the ith digit in the limit.
            less_than = sum(1 for d in digits if d < k)
            # We add this digit to every possible number of one less digit than
            # an i length number for each digit less than the ith digit in
            # limit.
            soln += (powers[i-1] * less_than)
            # If there is no digit equal to the ith digit, we must stop here.
            equal_to = k in digits
            if not equal_to:
                break
        return soln


def test_1():
    digits = ["1","3","5","7"]
    n = 100
    expected = 20
    assert Solution().atMostNGivenDigitSet(digits, n) == expected


def test_2():
    digits = ["1","4","9"]
    n = 1000000000
    expected = 29523
    assert Solution().atMostNGivenDigitSet(digits, n) == expected


def test_3():
    digits = ["1","3","5","7"]
    n = 372
    expected = 49
    assert Solution().atMostNGivenDigitSet(digits, n) == expected


def test_4():
    "WA"
    digits = ["3","4","8"]
    n = 4
    expected = 2
    assert Solution().atMostNGivenDigitSet(digits, n) == expected
