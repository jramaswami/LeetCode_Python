"""
LeetCode
1760. Minimum Limit of Balls in a Bag
December 2025 Challenge
jramaswami
"""


class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        max_bags = len(nums) + maxOperations
        
        def check(k):
            bags = 0
            for n in nums:
                bags += ceil(n / k)
            return bags <= max_bags

        lo = 1
        hi = max(nums)
        soln = hi
        while lo <= hi:
            k = lo + ((hi - lo) // 2)
            if check(k):
                soln = min(k, soln)
                hi = k - 1
            else:
                lo = k + 1
        return soln
