"""
LeetCode
7. Reverse Integer
jramaswami
"""


class Solution:
    def reverse(self, x: int) -> int:
        max_digits = [int(c) for c in str(pow(2,31))]
        digits = [0 for _ in max_digits]
        x0 = abs(x)
        for i, d in zip(range(len(digits)-1, -1, -1), str(abs(x))):
            digits[i] = int(d)

        # Subtract one for the positive limit
        if x > 0:
            max_digits[-1] -= 1

        for d, t in zip(digits, max_digits):
            if d > t:
                return 0
            if d < t:
                break

        sign = -1 if x < 0 else 1
        return (sign * int("".join(str(d) for d in digits)))




def test_1():
    x = 123
    expected = 321
    assert Solution().reverse(x) == expected


def test_2():
    x = -123
    expected = -321
    assert Solution().reverse(x) == expected


def test_3():
    x = 120
    expected = 21
    assert Solution().reverse(x) == expected


def test_4():
    x = (int(str(pow(2, 31))[::-1]))
    expected = 0
    print(pow(2,31))
    assert Solution().reverse(x) == expected


def test_5():
    x = -(int(str(pow(2, 31))[::-1]))
    expected = -pow(2, 31)
    assert Solution().reverse(x) == expected