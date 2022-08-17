"""
LeetCode :: 306. Additive Number
jramaswami
"""


class Solution:

    def isAdditiveNumber(self, num: str) -> bool:

        def solve(i, a, b):
            if i >= len(num):
                return True

            if num[i] == '0':
                # No leading zeros are allowed.
                return False

            c = 0
            for j in range(len(num)-1):
                c *= 10
                c += int(num[j])
                if a + b == c:
                    if solve(j+1, b, c):
                        return True
            return False

        # Initial two numbers.
        a = 0
        for i, x in enumerate(num):
            a *= 10
            a += int(x)
            if num[i+1] != '0':
                b = 0
                for j, y in enumerate(num[i+1:], start=i+1):
                    b *= 10
                    b += int(y)
                    if solve(j+1, a, b):
                        return True
        return False


def test_1():
    num = "112358"
    expected = True
    assert Solution().isAdditiveNumber(num) == expected


def test_2():
    num = "199100199"
    expected = True
    assert Solution().isAdditiveNumber(num) == expected


def test_3():
    "RTE"
    num = "0"
    expected = False
    assert Solution().isAdditiveNumber(num) == expected