"""
LeetCode
1432. Max Difference You Can Get From Changing an Integer
June 2025 Challenge
jramaswami
"""


class Solution:
    def maxDiff(self, num: int) -> int:
        S = str(num)
        # For minimum, replace the first value with zero
        multiplier = pow(10, len(S) - 1)
        min_value = 0
        for digit in S:
            if digit != S[0]:
                min_value += (multiplier * int(digit))
            multiplier //= 10

        # For maximum, replace first non-nine digit with 9
        multiplier = pow(10, len(S) - 1)
        max_value = 0
        replacing = None
        for digit in S:
            if digit == '9':
                max_value += (multiplier * 9)
            elif replacing:
                if digit == replacing:
                    max_value += (multiplier * 9)
                else:
                    max_value += (multiplier * int(digit))
            else:
                replacing = digit
                max_value += (multiplier * 9)
            multiplier //= 10

        # If the min number ends up as zero, then
        # substitute 1 instead. Since it ended up as zero
        # then all digits were the same and you substituted it out.
        if min_value == 0:
            min_value = int(''.join('1' for _ in S))

        return max_value - min_value


def test_1():
    num = 555
    expected = 888
    assert Solution().maxDiff(num) == expected


def test_2():
    num = 9
    expected = 8
    assert Solution().maxDiff(num) == expected


def test_3():
    "WA"
    num = 123456
    expected = 820000
    assert Solution().maxDiff(num) == expected