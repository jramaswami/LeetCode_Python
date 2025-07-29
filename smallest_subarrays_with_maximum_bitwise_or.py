"""
LeetCode
2411. Smallest Subarrays With Maximum Bitwise OR
July 2025 Challenge
jramaswami
"""


from typing import List


class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        # Compute an OR suffix array with the max or for B[i:j]
        # Also compute the minimum location of a given bit
        INF = pow(10, 10)
        min_bit_index = [[INF for _ in range(32)] for _ in nums]
        suffix = [0 for _ in nums]
        curr = 0
        for i in range(len(nums)-1, -1, -1):
            curr |= nums[i]
            suffix[i] = curr
            for b in range(32):
                mask = 1 << b
                if nums[i] & mask:
                    min_bit_index[i][b] = i
                elif i+1 < len(nums):
                    min_bit_index[i][b] = min_bit_index[i+1][b]

        soln = []
        for i, n in enumerate(nums):
            max_or = suffix[i]
            result = i
            for b in range(32):
                mask = 1 << b
                if mask & max_or:
                    result = max(result, min_bit_index[i][b])
            soln.append(result - i + 1)

        return soln


def test_1():
    nums = [1,0,2,1,3]
    expected = [3,3,2,2,1]
    assert Solution().smallestSubarrays(nums) == expected