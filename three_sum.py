"""
LeetCode :: October 2021 Challenge :: 15. 3Sum
jramaswami
"""


import collections


class Solution:
    def threeSum(self, nums):

        cache = collections.defaultdict(list)

        nums.sort()
        zero_count = 0
        for i, a in enumerate(nums):
            if a == 0:
                zero_count += 1
            for j, b in enumerate(nums[i+1:], start=i+1):
                cache[a + b].append((i, j))


        solns = set()
        if zero_count > 2:
            solns.add((0,0,0))

        for i, a in enumerate(nums):
            if a == 0:
                continue
            for j, k in cache[-a]:
                if i > j and i > k:
                    solns.add((a, nums[j], nums[k]))

        return [list(T) for T in solns]


def test_1():
    nums = [0] * 3000
    assert Solution().threeSum(nums) == [[0, 0, 0]]
