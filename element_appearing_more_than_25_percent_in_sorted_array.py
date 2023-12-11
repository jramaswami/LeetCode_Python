"""
LeetCode
1287. Element Appearing More Than 25% In Sorted Array
December 2023 Challenge
jramaswami
"""


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        curr = arr[0]
        freq = 1
        max_freq = 0
        soln = curr
        for n in arr[1:]:
            if n != curr:
                if freq > max_freq:
                    soln = curr
                    max_freq = freq
                curr = n
                freq = 1
            else:
                freq += 1
        if freq > max_freq:
            soln = curr
            max_freq = freq
        return soln