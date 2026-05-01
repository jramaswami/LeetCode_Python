"""
LeetCode
396. Rotate Function
May 2026 Challenge
jramaswami
"""


from typing import List


class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        # Let N be the length of nums
        N = len(nums)
        # Let T be the sum of all but the first element in F(k)
        T = sum(nums[1:])
        # Let F be the sum of F(k)
        F = sum(i * x for i, x in enumerate(nums))

        soln = F
        for i, x in enumerate(nums[:-1]):
            # x moves from the front where it add 0*n to F
            # to the back where it will add x(N-1)
            F += x * (N-1)
            # Every number moves left so we reduce F by T
            F -= T
            # See if F(k) such that x is the *last* number is the soln
            soln = max(soln, F)
            # x was excluded from T so add it back in
            T += x
            # nums[i+1] will now drop out of T
            T -= nums[i+1]
        return soln