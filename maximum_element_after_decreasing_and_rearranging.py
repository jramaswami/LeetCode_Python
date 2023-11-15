"""
LeetCode
1846. Maximum Element After Decreasing and Rearranging
November 2023 Challenge
jramaswami
"""


from typing import List


class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        soln = 1
        arr[0] = 1
        for i, _ in enumerate(arr[1:], start=1):
            arr[i] = min(arr[i], arr[i-1]+1)
            soln = max(soln, arr[i])
        return soln