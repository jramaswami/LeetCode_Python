"""
LeetCode
1340. Jump Game V
May 2026 Challenge
jramaswami
"""


from typing import List
import functools


class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        @functools.cache
        def rec(i):
            result = 1
            current_value = arr[i]
            # Left jumps
            for j in range(i-1, i-d-1, -1):
                if j < 0:
                    break
                jump_value = arr[j]
                if jump_value >= current_value:
                    break
                result = max(result, 1 + rec(j))
            # Right jumps
            for j in range(i+1, i+d+1):
                if j >= len(arr):
                    break
                jump_value = arr[j]
                if jump_value >= current_value:
                    break
                result = max(result, 1 + rec(j))
            return result

        return max(rec(i) for i, _ in enumerate(arr))