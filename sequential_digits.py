"""
LeetCode :: January 2022 Challenge :: Sequential Digits
jramaswami
"""


class Solution:

    def sequentialDigits(self, low, high):

        def solve(current, ones, low, high, acc):

            if low <= current <= high:
                acc.append(current)

            queue = []
            if ones + 1 < 10:
                current0 = (current * 10) + (ones + 1)
                if current0 <= high:
                    solve(current0, ones + 1, low, high, acc)

        acc = []
        # Check each starting number.
        for d in range(1, 10):
            solve(d, d, low, high, acc)
        return sorted(acc)


def test_1():
    low = 100
    high = 300
    expected = [123,234]
    assert Solution().sequentialDigits(low, high) == expected


def test_2():
    low = 1000
    high = 13000
    expected = [1234,2345,3456,4567,5678,6789,12345]
    assert Solution().sequentialDigits(low, high) == expected
