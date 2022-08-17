"""
LeetCode :: 306. Additive Number
jramaswami
"""


class Solution:

    def isAdditiveNumber(self, num: str) -> bool:

        def solve(i, a, b):
            if i >= len(num):
                return True

            if a + b == 0 and num[i] == '0':
                # No leading zeros are allowed, but 0 itself is allowed.
                return (i + 1, b, 0)

            c = 0
            for j, x in enumerate(num[i:], start=i):
                c *= 10
                c += int(x)
                if a + b < c:
                    return False
                if a + b == c:
                    if solve(j+1, b, c):
                        return True
            return False

        a = 0
        for i, x in enumerate(num[:-2]):
            a *= 10
            a += int(x)
            b = 0
            for j, y in enumerate(num[i+1:-1], start=i+1):
                b *= 10
                b += int(y)
                if j+1 < len(num):
                    if solve(j+1, a, b):
                        return True
                if b == 0:
                    # No leading zeros.
                    break
            if a == 0:
                # No leading zeros.
                break
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


def test_4():
    "WA"
    num = "111"
    expected = False
    assert Solution().isAdditiveNumber(num) == expected


def test_5():
    "WA"
    num = "101"
    expected = True
    assert Solution().isAdditiveNumber(num) == expected


def test_6():
    num = "000"
    expected = True
    assert Solution().isAdditiveNumber(num) == expected


def test_7():
    num = "0199100199"
    expected = False
    assert Solution().isAdditiveNumber(num) == expected


def test_8():
    "WA"
    num = "1203"
    expected = False
    assert Solution().isAdditiveNumber(num) == expected


if __name__ == '__main__':
    test_7()