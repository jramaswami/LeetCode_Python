"""
LeetCode
1437. Check If All 1's Are at Least Length K Places Away
November 2025 Challenge
jramaswami
"""


from typing import List


class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        prev = -pow(10, 10)
        for i, n in enumerate(nums):
            if n == 1:
                dist = i - prev - 1
                if dist < k:
                    return False
                prev = i
        return True