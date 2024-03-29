"""
LeetCode
1802. Maximum Value at a Given Index in a Bounded Array
June 2023
jramaswami
"""


class Solution:
    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        # Binary search the answer
        def summation(x):
            if x <= 0:
                return 0
            return (x * (x + 1)) // 2

        def check(guess):
            g = guess - 1
            left = summation(guess - 1) - summation(guess - 1 - index)
            right = summation(guess - 1) - summation(guess - 1 - (n - index - 1))
            left_fill = max(0, index + 1 - guess)
            right_fill = max(0, n - index - guess)
            total = guess + left + right + left_fill + right_fill
            # print(f"{left=} {right=} {guess=} {left_fill=} {right_fill=} {total=} {maxSum=}")
            if total <= maxSum:
                return True
            return False

        lo = 1
        hi = maxSum
        soln = 1
        while lo <= hi:
            mid = lo + ((hi - lo) // 2)
            if check(mid):
                soln = max(soln, mid)
                lo = mid + 1
            else:
                hi = mid - 1
        return soln



def test_1():
    n = 4
    index = 2
    maxSum = 6
    expected = 2
    assert Solution().maxValue(n, index, maxSum) == expected


def test_2():
    n = 6
    index = 1
    maxSum = 10
    expected = 3
    assert Solution().maxValue(n, index, maxSum) == expected


def test_3():
    "TLE"
    n = 3
    index = 0
    maxSum = 815094800
    expected = 271698267
    assert Solution().maxValue(n, index, maxSum) == expected


def test_4():
    "WA"
    n = 4
    index = 0
    maxSum = 4
    expected = 1
    assert Solution().maxValue(n, index, maxSum) == expected


def test_5():
    "WA"
    n = 3
    index = 2
    maxSum = 18
    expected = 7
    assert Solution().maxValue(n, index, maxSum) == expected