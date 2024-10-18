"""
LeetCode
2044. Count Number of Maximum Bitwise-OR Subsets
October 2024 Challenge
jramaswami
"""


import collections
import functools
import operator


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = functools.reduce(operator.or_, nums)
        soln = 0

        queue = collections.deque()
        queue.append((-1, 0))
        while queue:
            i, x = queue.popleft()
            j = i + 1
            if j < len(nums):
                y = x | nums[j]
                queue.append((j, y))
                if y == max_or:
                    soln += 1
                queue.append((j, x))
        
        return soln
