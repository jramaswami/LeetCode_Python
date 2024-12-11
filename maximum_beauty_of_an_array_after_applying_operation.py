"""
LeetCode
2779. Maximum Beauty of an Array After Applying Operation
December 2024 Challenge
jramaswami
"""


import collections
from typing import List


class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        soln = 0
        window = collections.deque()
        nums.sort()
        for n in nums:
            window.append(n)
            while window[-1] - window[0] > 2 * k:
                window.popleft()
            soln = max(soln, len(window))
        return soln
