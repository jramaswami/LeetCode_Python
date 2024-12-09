"""
LeetCode
3152. Special Array II
December 2024 Challenge
jramaswami
"""


import collections


class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        left = 0
        parity_ranges = []
        for i, _ in enumerate(nums[1:], start=1):
            if nums[i-1] % 2 == nums[i] % 2:
                # Parity is the same
                parity_ranges.append((left, i-1))
                left = i
        parity_ranges.append((left, len(nums)-1))
        
        queries0 = collections.deque(sorted((left, right, i) for i, (left, right) in enumerate(queries)))
        
        soln = [False for _ in queries]
        for left, right in parity_ranges:
            while queries0 and queries0[0][0] <= right:
                qleft, qright, i = queries0.popleft()
                if left <= qleft and qright <= right:
                    soln[i] = True
        return soln
