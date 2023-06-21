"""
LeetCode
2448. Minimum Cost to Make Array Equal
June 2023 Challenge
jramaswami
"""

from typing import List


class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        def compute_cost(x):
            return sum(abs(n - x) * c for n, c in zip(nums, cost))

        def ternary_search(f, left, right, eps):
            while abs(right - left) >= eps:
                left_third = left  + (right - left) / 3
                right_third = right - (right - left) / 3
                if f(left_third) > f(right_third):
                    left = left_third
                else:
                    right = right_third

            return (left + right) / 2

        best_x = ternary_search(compute_cost, min(nums), max(nums), 0.00000001)
        return compute_cost(round(best_x))


def test_1():
    nums = [1,3,5,2]
    cost = [2,3,1,14]
    expected = 8
    assert Solution().minCost(nums, cost) == expected


def test_2():
    nums = [2,2,2,2,2]
    cost = [4,2,8,1,3]
    expected = 0
    assert Solution().minCost(nums, cost) == expected


def test_3():
    "WA"
    nums = [576257,268115,512826,523563,927189,39253,720661,35147,552624,847824,354489,760949,734966,571013]
    cost = [842872,273313,503060,139143,367612,217125,271272,407727,199063,120280,819193,935689,624116,453146]
    expected = 1122145265809
    assert Solution().minCost(nums, cost) == expected
