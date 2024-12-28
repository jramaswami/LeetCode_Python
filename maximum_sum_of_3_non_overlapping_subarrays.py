"""
LeetCode
689. Maximum Sum of 3 Non-Overlapping Subarrays
December 2024 Challenge
jramawami

Thank You NeetCode.IO!
"""


from typing import List
import collections


class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        # Compute k sums
        ksums = [sum(nums[:k])]
        for i in range(k, len(nums)):
            ksums.append(ksums[-1]+nums[i]-nums[i-k])
        
        # Memoization
        cache = dict()

        def get_max_sum(i, cnt):
            # Base case
            if cnt == 3 or i > len(nums) - k:
                return 0
            
            # Recursive case
            key = (i, cnt)
            if key not in cache:
                include = ksums[i] + get_max_sum(i + k, cnt + 1)
                skip = get_max_sum(i+1, cnt)
                cache[key] = max(include, skip)
            return cache[key]

        
        def get_indices():
            i = 0
            indices = []
            while i <= len(nums) - k and len(indices) < 3:
                include = ksums[i] + get_max_sum(i+k, len(indices)+1)
                skip = get_max_sum(i+1, len(indices))

                if include >= skip:
                    indices.append(i)
                    i += k
                else:
                    i += 1

            return indices
        
        return get_indices()


def test1():
    nums = [1,2,1,2,6,7,5,1]
    k = 2
    expected = [0,3,5]
    assert Solution().maxSumOfThreeSubarrays(nums, k) == expected
