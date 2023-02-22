"""
LeetCode
1011. Capacity To Ship Packages Within D Days
February 2023 Challenge
jramaswami
"""


from typing import *


class Solution:
    def shipWithinDays(self, weights: List[int], max_days: int) -> int:

        def check(capacity):
            shipping_days = 1
            curr_weight = weights[0]
            for x in weights[1:]:
                if x + curr_weight > capacity:
                    shipping_days += 1
                    curr_weight = x
                else:
                    curr_weight += x
            return shipping_days <= max_days

        lo = max(weights)
        hi = sum(weights)
        soln = hi
        while lo <= hi:
            mid = lo + ((hi - lo) // 2)
            if check(mid):
                soln = min(soln, mid)
                hi = mid - 1
            else:
                lo = mid + 1
        return soln


def test_1():
    weights = [1,2,3,4,5,6,7,8,9,10]
    days = 5
    expected = 15
    assert Solution().shipWithinDays(weights, days) == expected


def test_2():
    weights = [3,2,2,4,1,4]
    days = 3
    expected = 6
    assert Solution().shipWithinDays(weights, days) == expected


def test_3():
    weights = [1,2,3,1,1]
    days = 4
    expected = 3
    assert Solution().shipWithinDays(weights, days) == expected