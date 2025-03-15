"""
LeetCode
2560. House Robber IV
March 2025 Challenge
jramaswami
"""


from typing import List


class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def check(capability):
            i = 0
            count = 0
            while i < len(nums):
                if nums[i] <= capability:
                    i += 2
                    count += 1
                else:
                    i += 1
                if count == k:
                    break
            return count == k

        soln = pow(10,10)
        low = min(nums)
        high = max(nums)
        while low <= high:
            mid = low + ((high - low) // 2)
            if check(mid):
                soln = min(soln, mid)
                high = mid - 1
            else:
                low = mid + 1
        return soln


def test_1():
    nums = [2,3,5,9]
    k = 2
    assert Solution().minCapability(nums, k) == 5