"""
LeetCode
2438. Range Product Queries of Powers
August 2025 Challenge
jramaswami
"""


from typing import List


class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        MOD = pow(10, 9) + 7
        # Get the powers of two that sum to n
        # Which is really just the bits that are on
        nums = []
        for bit in range(32):
            mask = 1 << bit
            if mask & n:
                nums.append(mask)

        soln = []
        for left, right in queries:
            product = 1
            for x in nums[left:right+1]:
                product *= x
                product %= MOD
            soln.append(product % MOD)
        return soln


def test_1():
    n = 15
    queries = [[0,1],[2,2],[0,3]]
    expected =  [2,4,64]
    assert Solution().productQueries(n, queries) == expected


def test_2():
    n = 2
    queries = [[0,0]]
    expected =  [2]
    assert Solution().productQueries(n, queries) == expected