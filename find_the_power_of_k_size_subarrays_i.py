"""
LeetCode
3254. Find the Power of K-Size Subarrays I
November 2024 Challenge
jramaswami
"""


class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        soln = []
        for i in range(len(nums) - k + 1):
            is_sorted = True
            for j in range(i+1, i+k):
                if nums[j] != nums[j-1]+1:
                    is_sorted = False
                    break
            if is_sorted:
                soln.append(nums[i+k-1])
            else:
                soln.append(-1)
        return soln
