"""
LeetCode
2615. Sum of Distances
April 2026 Challenge
jramaswami
"""


import collections
from typing import List


class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        soln = [0 for _ in nums]
        freq = collections.defaultdict(int)
        dist = collections.defaultdict(int)
        for i, x in enumerate(nums):
            if x in freq:
                soln[i] += ((freq[x] * i) - dist[x])
            dist[x] += i
            freq[x] += 1
        freq = collections.defaultdict(int)
        dist = collections.defaultdict(int)
        for i in range(len(nums) - 1, -1, -1):
            x = nums[i]
            if x in freq:
                soln[i] += (dist[x] - (freq[x] * i))
            dist[x] += i
            freq[x] += 1
        return soln