"""
LeetCode
1526. Minimum Number of Increments on Subarrays to Form a Target Array
October 2025 Challenge
jramaswami
"""


from typing import List


class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        soln = curr = 0
        for n in target:
            if curr < n:
                soln += n - curr
            curr = n
        return soln