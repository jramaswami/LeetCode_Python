"""
LeetCode
769. Max Chunks To Make Sorted
December 2024 Challenge
jramaswami
"""


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        soln = 0
        left = 0
        for right, n in enumerate(arr):
            # For arr[left:right+1], do we have all the numbers [left:right] (inclusive)
            included = set(arr[left:right+1])
            needed = set(range(left, right+1))
            # If we have what we need, then include the partition in the solution
            # and move the left pointer to right + 1 
            if included == needed:
                soln += 1
                left = right+1
        return soln
