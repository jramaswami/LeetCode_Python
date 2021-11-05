"""
LeetCode :: November 2021 Challenge :: 441. Arranging Coins
jramaswami
"""


class Solution:
    def arrangeCoins(self, n):
        lo = 0
        hi = 92682
        soln = 0
        while lo <= hi:
            mid = lo + ((hi - lo) // 2)
            k = ((mid * (mid + 1)) // 2)
            if k == n:
                return mid
            elif k < n:
                lo = mid + 1
                soln = max(mid, soln)
            else:
                hi = mid - 1
        return soln


def test_1():
    assert Solution().arrangeCoins(5) == 2


def test_2():
    assert Solution().arrangeCoins(8) == 3