"""
LeetCode
898. Bitwise ORs of Subarrays
July 2025 Challenge
jramaswami

REF: https://algo.monster/liteproblems/898
"""


from typing import List


class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        ors = set()
        prev = 0
        for i, n in enumerate(arr):
            prev |= n
            curr = 0
            for j in range(i, -1, -1):
                curr |= arr[j]
                ors.add(curr)
                if curr == prev:
                    break
        return len(ors)
