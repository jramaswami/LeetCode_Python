"""
LeetCode :: January 2022 Challenge :: 8. String to Integer (atoi)
jramaswami
"""


class Solution:

    def myAtoi(self, S):

        sign = 1
        number = 0
        i = 0
        # Step 1: read and ignore whitespace.
        while i < len(S) and S[i].isspace():
            i += 1
        # Step 2: read a + or - sign.
        if i < len(S) and S[i] in '+-':
            if S[i] == '-':
                sign = -1
            i += 1
        # Step 3: read next characters until the next nondigit or end of input.
        # Step 4: convert these numbers into an integer, change sign if
        # necessary.
        while i < len(S) and S[i].isdigit():
            number *= 10
            number += int(S[i])
            i +=1
        number *= sign
        # Step 5: clamp to 32-bit integer.
        limit = pow(2, 31)
        number = max(number, -limit)
        number = min(number, limit-1)
        return number


def test_1():
    S = "42"
    expected = 42
    assert Solution().myAtoi(S) == expected


def test_2():
    S = "   -42"
    expected = -42
    assert Solution().myAtoi(S) == expected


def test_3():
    S = "4193 with words"
    expected = 4193
    assert Solution().myAtoi(S) == expected


def test_4():
    S = "   -99999999999999999999999999999999999999999"
    expected = -pow(2,31)
    assert Solution().myAtoi(S) == expected


def test_5():
    S = "   99999999999999999999999999999999999999999 xxx"
    expected = pow(2,31)-1
    assert Solution().myAtoi(S) == expected
