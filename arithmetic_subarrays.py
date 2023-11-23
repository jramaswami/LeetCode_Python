"""
LeetCode
1630. Arithmetic Subarrays
November 2023 Challenge
jramaswami
"""


class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        def is_arithmetic_sequence(A):
            if len(A) < 2:
                return False
            delta = A[0] - A[1]
            return all(a - b == delta for a, b in zip(A[:-1], A[1:]))

        return [is_arithmetic_sequence(list(sorted(nums[a:b+1]))) for a, b in zip(l, r)]