"""
LeetCode
2163. Minimum Difference in Sums After Removal of Elements
July 2025 Challenge
jramaswami
"""


import heapq
import math
from typing import List


class Solution:
    def minimumDifference(self, nums: List[int]) -> int:
        # Use heapq to find the minimum sum of n numbers from nums[:i]
        n = len(nums) // 3
        min_sum = 0
        min_heap = []
        min_prefix = [math.inf for _ in nums]
        for i, x in enumerate(nums):
            if len(min_heap) == n:
                min_prefix[i] = min_sum
            # Add to heap and sum
            min_sum += x
            # Heap should have largest values first, so -x
            heapq.heappush(min_heap, -x)
            while len(min_heap) > n:
                # Remove the largest item
                y = -heapq.heappop(min_heap)
                # Subtract it from the sum
                min_sum -= y

        # Use heapq to find the maximum sum of n numbers from nums[i:]
        max_heap = []
        max_sum = 0
        max_prefix = [-math.inf for _ in nums]
        for i in range(len(nums)-1, -1, -1):
            x = nums[i]
            # Add to heap and sum
            max_sum += x
            heapq.heappush(max_heap, x)
            while len(max_heap) > n:
                # Remove smallest item
                y = heapq.heappop(max_heap)
                max_sum -= y
            if len(max_heap) == n:
                max_prefix[i] = max_sum

        return min(a - b for a, b in zip(min_prefix, max_prefix))