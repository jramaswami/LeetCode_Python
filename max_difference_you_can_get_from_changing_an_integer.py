"""
LeetCode
1432. Max Difference You Can Get From Changing an Integer
June 2025 Challenge
jramaswami
"""


class Solution:
    def maxDiff(self, num: int) -> int:

        S = str(num)
        # For minimum, replace first non-one digit with 1
        multiplier = pow(10, len(S) - 1)
        min_value = 0
        replacing = None
        replace_with = '1'
        if S[0] == '1':
            replace_with = '0'
        for i, digit in enumerate(S):
            if replace_with == '0' and digit == '1':
                min_value += (multiplier * int(digit))
            elif digit == replace_with:
                min_value += (multiplier * int(replace_with))
            elif replacing:
                if digit == replacing:
                    min_value += (multiplier * int(replace_with))
                else:
                    min_value += (multiplier * int(digit))
            else:
                replacing = digit
                min_value += (multiplier * int(replace_with))
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


def test_4():
    "WA"
    num = 111
    expected = 888
    assert Solution().maxDiff(num) == expected