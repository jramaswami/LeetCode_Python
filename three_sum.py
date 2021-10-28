"""
LeetCode :: October 2021 Challenge :: 15. 3Sum
jramaswami
"""


import collections


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        cache = collections.defaultdict(list)

        nums.sort()
        for i, a in enumerate(nums):
            for j, b in enumerate(nums[i+1:], start=i+1):
                cache[a + b].append((i, j))

        solns = set()
        for i, a in enumerate(nums):
            for j, k in cache[-a]:
                if i > j and i > k:
                    solns.add((a, nums[j], nums[k]))

        return solns
