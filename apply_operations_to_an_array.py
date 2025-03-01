"""
LeetCode
2460. Apply Operations to an Array
March 2025 Challenge
jramaswami
"""


class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i, _ in enumerate(nums[:-1]):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
        soln = [x for x in nums if x]
        soln.extend(0 for _ in range(len(nums) - len(soln)))
        return soln          
