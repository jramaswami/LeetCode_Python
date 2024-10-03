"""
LeetCode
1590. Make Sum Divisible by P
October 2024 Challenge
jramaswami

Thank You NeetCodeIO!
"""


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        # Get total modulo p
        T = 0
        for i, n in enumerate(nums):
            T += n
            T %= p
        
        # If total sum is divisible by p, return  0.
        if T == 0:
            return 0
        
        # Iterate over nums keeping track of prefix sums 
        # at the position we last saw it
        soln = len(nums)
        curr_sum = 0
        seen = dict()
        # Intialize prefix sum of zero at position before 
        #beginning of nums
        seen[0] = -1
        for i, n in enumerate(nums):
            curr_sum += n
            curr_sum %= p
            
            # Compute the prefix sum that when removed will
            # result in the sum(nums[j:i+1]) % p == 0, if
            # it exists
            x = (curr_sum - T + p) % p
            if x in seen:
                j = seen[x]
                soln = min(soln, i-j)
            
            # Add curr prefix sum to seen, since this is
            # the last time we saw it
            seen[curr_sum] = i

        # If we removed the entire array, return -1
        return -1 if soln == len(nums) else soln
