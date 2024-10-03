"""
LeetCode
1590. Make Sum Divisible by P
October 2024 Challenge
jramaswami
"""


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        # Take prefix sums modulo p
        prefix = [None for _ in nums]
        curr_sum = 0
        for i, n in enumerate(nums):
            curr_sum += n
            curr_sum %= p
            prefix[i] = curr_sum
        
        if curr_sum == 0:
            return 0

        # Get function to return the sum a subarray [left:right] (inclusive)
        def get(left, right):
            if left == 0:
                return prefix[right]
            return (prefix[right] - prefix[left-1] + p) % p

        # Check each subarray
        soln = len(nums) + 10
        for left in range(len(nums)):
            for right in range(left, len(nums)):
                # Do not remove the entire array
                if left == 0 and right == len(nums) - 1:
                    continue
                x = get(left, right)
                y = (curr_sum - x + p) % p
                if y == 0:
                    soln = min(soln, (right - left + 1))
        return -1 if soln == len(nums) + 10 else soln
