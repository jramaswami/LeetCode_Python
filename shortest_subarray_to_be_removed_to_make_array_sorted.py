"""
LeetCode
1574. Shortest Subarray to be Removed to Make Array Sorted
November 2024 Challenge
jramaswami
"""


import bisect


class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        
        left = [arr[0]]
        for x in arr[1:]:
            if x < left[-1]:
                break
            left.append(x)
        soln = len(left)

        if len(left) != len(arr):
            right = [arr[-1]]
            for x in reversed(arr[:-1]):
                if x > right[-1]:
                    break
                right.append(x)
            right = right[::-1]
            soln = max(soln, len(right))

            # Only do this if there is a gap between left and right
            for j, x in enumerate(left):
                i = bisect.bisect_left(right, x)
                y = '-' if i >= len(right) else right[i]            
                len_left = j + 1
                len_right = len(right) - i
                soln = max(soln, len_left + len_right)
        return len(arr) - soln
