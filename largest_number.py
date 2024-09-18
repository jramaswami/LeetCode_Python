"""
LeetCode
179. Largest Number
September 2024 Challenge
jramaswami
"""


import collections
import functools


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def compare(a, b):
            x = int(a+b)
            y = int(b+a)
            if x <= y:
                return 1
            return -1

        nums0 = [str(t) for t in nums]
        nums0.sort(key=functools.cmp_to_key(compare))
        nums1 = collections.deque(nums0)
        while len(nums1) > 1 and int(nums1[0]) == 0:
            nums1.popleft()
        return "".join(nums1)
