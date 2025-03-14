"""
LeetCode
2226. Maximum Candies Allocated to K Children
March 2025 Challenge
jramaswami
"""


from typing import List


class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def check(pile_size, child_count):
            for pile in candies:
                pile_count = pile // pile_size
                child_count -= pile_count
            return child_count <= 0

        # binary search the answer
        low = 1
        high = max(candies)
        soln = 0
        while low <= high:
            mid = low + ((high - low) // 2)
            if check(mid, k):
                soln = max(soln, mid)
                low = mid + 1
            else:
                high = mid - 1
        return soln


def test_1():
    candies = [5,8,6]
    k = 3
    expected = 5
    assert Solution().maximumCandies(candies, k) == expected


def test_2():
    candies = [2,5]
    k = 11
    expected = 0
    assert Solution().maximumCandies(candies, k) == expected


def test_3():
    candies = [3102006,6279432,7216621,3628028,5711306,2292506,2107393]
    k = 23626985
    expected = 1
    assert Solution().maximumCandies(candies, k) == expected