"""
LeetCode :: March 2022 Challenge :: 1359. Count All Valid Pickup and Delivery Options
jramaswami


Thank You Larry!
"""


class Solution:

    def countOrders(self, n):

        MOD = pow(10, 9) + 7
        soln = 1
        for k in range(2, n+1):
            prev = (2 * (k-1))
            pickup = prev + 1
            total = (pickup * (pickup+1)) // 2
            soln = ((soln * total) % MOD)
        return soln


def test_1():
    n = 1
    expected = 1
    assert Solution().countOrders(n) == expected


def test_2():
    n = 2
    expected = 6
    assert Solution().countOrders(n) == expected


def test_3():
    n = 3
    expected = 90
    assert Solution().countOrders(n) == expected
