"""
LeetCode
3350. Adjacent Increasing Subarrays Detection II
October 2025 Challenge
jramaswami
"""


from typing import List


class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        # Binary search the answer
        def check(k):
            suffix = [0 for _ in nums]
            suffix[-1] = 1
            for i in range(len(nums)-2, -1, -1):
                if nums[i] < nums[i+1]:
                    suffix[i] = suffix[i+1] + 1
                else:
                    suffix[i] = 1

            curr = 0
            for i in range(len(nums)-1):
                if i == 0 or nums[i-1] < nums[i]:
                    curr += 1
                else:
                    curr = 1
                if curr >= k and suffix[i+1] >= k:
                    return True
            return False

        soln = 0
        low = 0
        high = len(nums)
        while low <= high:
            mid = low + (high - low) // 2
            if check(mid):
                soln = max(soln, mid)
                low = mid + 1
            else:
                high = high - 1
        return soln