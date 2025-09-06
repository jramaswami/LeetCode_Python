"""
LeetCode
3495. Minimum Operations to Make Array Elements Zero
September 2025 Challenge
jramaswami

REF: https://www.youtube.com/watch?v=WnCgm3ZouFU
"""


from typing import List


class Solution:
    def minOperations(self, queries: List[List[int]]) -> int:
        soln = 0
        for l, r in queries:
            ops, start, end = 0, 1, 4
            # 10^9 < 4^16
            # Let d = the number of operations to reduce to zero
            for d in range(1, 16):
                # Get the left and right of the numbers that require
                # d operations to reduce to zero
                left = max(l, start)
                right = min(r, end-1)
                if right >= left:
                    # Compute how many numbers there are in the range
                    n = right - left + 1
                    # Perform the d operations on those numbers
                    ops += (n * d)
                # Move to next range
                start *= 4
                end *= 4

            soln += math.ceil(ops / 2)
        return soln