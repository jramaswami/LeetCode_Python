"""
LeetCode
3355. Zero Array Transformation I
May 2025 Challenge
jramaswami
"""


class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        running_delta = [0 for _ in range(len(nums)+1)]
        for left, right in queries:
            running_delta[left] -= 1
            running_delta[right+1] += 1

        result = list(nums)
        curr_delta = 0
        for i, _ in enumerate(result):
            curr_delta += running_delta[i]
            result[i] += curr_delta
        return all(x <= 0 for x in result)